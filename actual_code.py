import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from ipywidgets import interact, widgets
from IPython.display import display, HTML, clear_output

class SkylinePro:
    def __init__(self, api_key):
        self.api_key = api_key
        # Updated to the correct endpoint
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.log_file = "weather_history.csv"
        self.cities = sorted(["Mumbai", "Bengaluru", "New York", "London", "Tokyo", "Singapore", "Sydney", "Dubai"])
        
        # Initialize CSV if it doesn't exist
        try:
            pd.read_csv(self.log_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Timestamp", "City", "Temp", "Feels_Like", "Humidity", "Wind_Speed"])
            df.to_csv(self.log_file, index=False)

    def fetch_and_log(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "City": city,
                "Temp": data['main']['temp'],
                "Feels_Like": data['main']['feels_like'],
                "Humidity": data['main']['humidity'],
                "Wind_Speed": data['wind']['speed']
            }
            
            # Save to CSV
            df = pd.DataFrame([weather_data])
            df.to_csv(self.log_file, mode='a', header=False, index=False)
            
            # Display UI
            self.display_ui(weather_data)
        else:
            print("Error: Check API Key or City Name.")

    def display_ui(self, d):
        clear_output(wait=True)
        html = f"""
        <div style="background-color: #121212; color: #00FF41; padding: 20px; border-radius: 10px; font-family: monospace;">
            <h3>> SYSTEM_LOG: {d['City']} @ {d['Timestamp']}</h3>
            <p>TEMPERATURE: {d['Temp']}°C (Feels like {d['Feels_Like']}°C)</p>
            <p>HUMIDITY: {d['Humidity']}%</p>
            <p>WIND_SPEED: {d['Wind_Speed']} m/s</p>
            <p style="color: #888;">Data saved to {self.log_file}</p>
        </div>
        """
        display(HTML(html))
        self.show_plot(d)

    def show_plot(self, d):
        metrics = ['Temp', 'Feels_Like', 'Humidity']
        values = [d['Temp'], d['Feels_Like'], d['Humidity']]
        
        plt.figure(figsize=(6, 3))
        plt.bar(metrics, values, color=['#1e88e5', '#ffb300', '#43a047'])
        plt.title(f"Weather Metrics for {d['City']}")
        plt.ylabel("Value")
        plt.show()

    def run(self):
        interact(self.fetch_and_log, city=widgets.Dropdown(options=self.cities, description="Target City:"))

# Function to download data in Colab
def download_data():
    from google.colab import files
    files.download('weather_history.csv')
