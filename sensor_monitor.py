import random
import numpy as np
SEED = 42

def ask_float(prompt): # comma getal
    while True:
        text=input(prompt)
        try:
            return float(text)
        except ValueError:
            print("Please enter a valid number.")

def ask_int(prompt): #positief getal
    while True:
        text=input(prompt)
        try:
            value = int(text)
        except ValueError:
            print(f"'{text}' is not a valid integer.")
            continue
        if value <= 0:
            print("Please enter a positive integer.")
            continue
        return value   

def get_input():
    sensor_type = input("sensor type (temperature, light): ")
    count = ask_int("Number of readings: ")
    while True:
        min_value = ask_float("Minimum value: ")
        max_value = ask_float("Maximum value: ")
        if min_value < max_value:
            break
        print("Minimum value must be less than maximum value.")
    threshold = ask_float("Threshold value: ")
    return {
        "sensor_type": sensor_type,
        "count": count,
        "min_value": min_value,
        "max_value": max_value,
        "threshold": threshold
    }
    
def generate_readings(count, min_value, max_value):
    random.seed(SEED)
    readings = []
    for _ in range(count):
        value = random.uniform(min_value, max_value)
        readings.append(round(value, 2))
    return np.array(readings)

def main():
    print("=== Sensor Data Analysis Tool ===")
    settings = get_input()
    readings = generate_readings(
        settings["count"], settings["min_value"], settings["max_value"]
    )
    print(readings)


if __name__ == "__main__":
    main()
