import requests
import json
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def get_current_temperature():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=bca0ae8b47144b88a6b143548240301&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = json.loads(response.text)
        temperature_celsius = weather_data["current"]["temp_c"]
        result_label.config(text=f"Current Temperature in {city}: {temperature_celsius}°C")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve weather data: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Weather Checker")

# Create and place widgets
city_label = Label(app, text="Enter the name of the city:")
city_label.pack(pady=10)

city_entry = Entry(app)
city_entry.pack(pady=10)

check_button = Button(app, text="Check Weather", command=get_current_temperature)
check_button.pack(pady=10)

result_label = Label(app, text="")
result_label.pack(pady=10)

# Run the application
app.mainloop()
