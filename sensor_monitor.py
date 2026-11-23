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

def calculate_statistics(readings, threshold):
    return {
        "count": len(readings),
        "mean": np.mean(readings),
        "min": np.min(readings),
        "max": np.max(readings),
        "std": np.std(readings),
        "above": np.sum(readings > threshold),
    }

def find_outliers(readings, threshold):
    return np.where(readings > threshold)[0]

def main():
    print("=== Sensor Data Analysis Tool ===")
    settings = get_input()
    readings = generate_readings(
        settings["count"], settings["min_value"], settings["max_value"]
    )

    threshold = settings["threshold"]
    stats = calculate_statistics(readings, threshold)
    outliers = find_outliers(readings, threshold)

    print(f"\n--- Statistics for {settings['sensor_type']} ---")
    print(f"Number of readings : {stats['count']}")
    print(f"Mean               : {stats['mean']:.2f}")
    print(f"Minimum            : {stats['min']:.2f}")
    print(f"Maximum            : {stats['max']:.2f}")
    print(f"Standard deviation : {stats['std']:.2f}")#getallen achter de komma
    print(f"Above threshold    : {stats['above']}")

    print("\nReadings above the threshold:")
    for i in outliers:
        print(f"  Sample {i + 1}: {readings[i]:.2f}")


if __name__ == "__main__":
    main()

