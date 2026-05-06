import requests
from ipywidgets import interact, widgets
from IPython.display import display, HTML

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.data.openweathermap.org/data/2.5/weather"
        self.cities = [
            "Mumbai", "Bengaluru", "New York", "London", "Tokyo", 
            "Paris", "Berlin", "Dubai", "Singapore", "Sydney", 
            "Toronto", "Moscow", "Shanghai", "Sao Paulo", "Cairo",
            "Istanbul", "Seoul", "Mexico City", "Jakarta", "Lagos",
            "Bangkok", "Chicago", "Madrid", "Rome", "Amsterdam"
        ]

    def fetch_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                desc = data['weather'][0]['description'].capitalize()
                
                # Professional HTML output for Colab
                output = f"""
                <div style="border: 2px solid #1e88e5; padding: 15px; border-radius: 10px; background-color: #f5f5f5; color: #333;">
                    <h2 style="margin-top:0;">📍 {city}</h2>
                    <p><b>🌡️ Temperature:</b> {temp}°C</p>
                    <p><b>💧 Humidity:</b> {humidity}%</p>
                    <p><b>☁️ Condition:</b> {desc}</p>
                </div>
                """
                display(HTML(output))
            else:
                print(f"❌ Error: {data.get('message', 'Unknown Error')}")
        except Exception as e:
            print(f"⚠️ Connection Error: {e}")

    def run(self):
        print("🌍 Skyline Weather Dashboard")
        interact(self.fetch_weather, city=widgets.Dropdown(options=sorted(self.cities), description="Select City:"))

# To run this in Colab, you would do:
# from actual_code import WeatherApp
# app = WeatherApp("YOUR_API_KEY")
# app.run()
