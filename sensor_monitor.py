import random
import numpy as np
import matplotlib.pyplot as plt
import csv

SEED = 42
CSV_FILE = "sensor_readings.csv"

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

def plot_readings(readings, threshold, sensor_type):
    samples = range(1, len(readings) + 1)
    plt.figure()
    plt.plot(samples, readings, marker="o", label="Readings")
    plt.axhline(y=threshold, color="red", linestyle="--", label="Threshold")
    plt.title(f"{sensor_type} readings")
    plt.xlabel("Sample number")
    plt.ylabel("Value")
    plt.grid(True)
    plt.legend()
    plt.savefig("readings_plot.png")

def plot_histogram(readings, sensor_type):
    plt.figure()
    plt.hist(readings, bins=10, edgecolor="black", label="Readings")
    plt.title(f"Distribution of {sensor_type} readings")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.legend()
    plt.savefig("readings_histogram.png")

def save_readings(readings, filename):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["sample", "reading"])
            for number, value in enumerate(readings, start=1):
                writer.writerow([number, value])
        print(f"\nReadings saved to {filename}")
    except OSError as error:
        print(f"\nError: could not save {filename}: {error}")

def main():
    print("=== Sensor Data Analysis Tool ===")
    settings = get_input()
    readings = generate_readings(
        settings["count"], settings["min_value"], settings["max_value"]
    )
    save_readings(readings, CSV_FILE)

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

    plot_readings(readings, threshold, settings["sensor_type"])
    plot_histogram(readings, settings["sensor_type"])
    plt.show()


if __name__ == "__main__":
    main()

