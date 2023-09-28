import pandas as pd
from matplotlib import pyplot as plt
import my_statistics as stats
import click


def read_data_from_file(file_name, num_measurements: int, column_name) -> list[float]:
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column_name]

def plot_temperatures(temperatures, mean, outputfile):
    plt.xlabel("Number of measurement")
    plt.ylabel("Air temperatures")
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(outputfile)
    plt.clf()


@click.command()
@click.option('--num_measurements', help='Number of temperatures to read and plot', type=int, required=True)
@click.option('--inputfile', help='The input data file name', required=True)
@click.option('--outputfile', help='The output image file name', required=True)
def main(num_measurements, inputfile, outputfile):
    temperatures = read_data_from_file(
        inputfile,
        num_measurements,
        "Air temperature (degC)"
    )

    mean = stats.compute_statistics(temperatures)

    plot_temperatures(temperatures, mean, outputfile)


if __name__ == '__main__':
    main()
    