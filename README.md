# Skyline Weather Analytics ☁️

A sleek, interactive weather dashboard designed specifically for Google Colab. This project leverages the OpenWeatherMap API to fetch real-time atmospheric data for 25 major global cities.

## 🚀 Overview
Traditional Python GUI libraries (like Tkinter) don't work in cloud environments. This project uses `ipywidgets` to create a seamless, web-native interface directly inside your Colab notebook.

## 📊 Features
- **Real-time Data:** Fetches current temperature and humidity.
- **Global Reach:** Pre-configured for 25 major business and cultural hubs.
- **Colab Optimized:** Uses interactive widgets instead of desktop windows.
- **Extensible:** Designed to be easily integrated into larger data science pipelines.

## 🚀 Pro Features
- **Advanced Metrics:** Fetches temperature, humidity, wind speed, and "feels like" data.
- **Persistent Storage:** Every query is logged to `weather_history.csv` for future analysis.
- **Analytics Engine:** Instant visualization of current weather data using Matplotlib.
- **Local Sync:** One-click download of your historical weather logs.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Environment:** Google Colab
- **API:** [OpenWeatherMap](https://openweathermap.org/)
- **Libraries:** `requests`, `ipywidgets`, `pandas`
- **Requests:** API communication.
- **Pandas:** Data manipulation and CSV management.
- **Matplotlib:** Data visualization.
- **IPython/Widgets:** Interactive Cloud UI.
