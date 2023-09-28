import pandas as pd
from matplotlib import pyplot as plt

def read_data_from_file(file_name, num_measurements: int, column_name) -> list[float]:
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column_name]

def compute_statistics(temperatures: list[float], num_measurements: int) -> float:
    mean = sum(temperatures) / num_measurements
    return mean

def plot_temperatures(temperatures, mean, num_measurements):
    plt.xlabel("Number of measurement")
    plt.ylabel("Air temperatures")
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(f"{num_measurements}.png")
    plt.clf()


for num_measurements in [25, 100, 500]:
    temperatures = read_data_from_file(
        "temperatures.csv",
        num_measurements,
        "Air temperature (degC)"
    )

    mean = compute_statistics(temperatures, num_measurements)

    plot_temperatures(temperatures, mean, num_measurements)
