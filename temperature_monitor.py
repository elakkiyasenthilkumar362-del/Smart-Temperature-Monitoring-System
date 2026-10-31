
import random
import time
import csv
from datetime import datetime

# Temperature monitoring system

THRESHOLD = 35

def read_temperature():
    # Simulated sensor reading
    temperature = round(random.uniform(25, 45), 2)
    return temperature

def check_temperature(temp):
    if temp > THRESHOLD:
        return "WARNING: HIGH TEMPERATURE!"
    else:
        return "NORMAL"

def save_data(temp, status):
    with open("temperature_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            temp,
            status
        ])

def main():
    print("SMART TEMPERATURE MONITORING SYSTEM")
    print("-----------------------------------")

    while True:
        temperature = read_temperature()
        status = check_temperature(temperature)

        print(f"Temperature: {temperature} °C")
        print(f"Status: {status}")
        print("-----------------------------------")

        save_data(temperature, status)

        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
