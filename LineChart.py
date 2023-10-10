import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

# Define a class for creating line charts
class LineChart:
    def __init__(self, title="", x_label="", y_label=""):
        """
        Initialize a LineChart object.

        :param title: Title of the chart.
        :param x_label: Label for the X-axis.
        :param y_label: Label for the Y-axis.
        """
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.x_data = []         # List to store X-axis data points.
        self.y_data = []         # List to store Y-axis data points.
        self.x_formatter = None  # Custom formatter for X-axis ticks.
        self.y_formatter = None  # Custom formatter for Y-axis ticks.

    def add_data(self, x_values, y_values):
        """
        Add data points to the chart.

        :param x_values: List of X-axis data points.
        :param y_values: List of Y-axis data points.
        """
        self.x_data.extend(x_values)
        self.y_data.extend(y_values)

    def set_title(self, title):
        """
        Set the chart title.

        :param title: Title of the chart.
        """
        self.title = title

    def set_x_label(self, x_label):
        """
        Set the label for the X-axis.

        :param x_label: Label for the X-axis.
        """
        self.x_label = x_label

    def set_y_label(self, y_label):
        """
        Set the label for the Y-axis.

        :param y_label: Label for the Y-axis.
        """
        self.y_label = y_label

    def set_x_formatter(self, func):
        """
        Set a custom formatter for the X-axis ticks.

        :param func: A function that formats X-axis tick labels.
        """
        self.x_formatter = FuncFormatter(func)

    def set_y_formatter(self, func):
        """
        Set a custom formatter for the Y-axis ticks.

        :param func: A function that formats Y-axis tick labels.
        """
        self.y_formatter = FuncFormatter(func)

    def save_chart(self, filename, format='png'):
        """
        Save the chart to a file.

        :param filename: Name of the file to save the chart.
        :param format: File format for saving the chart (e.g., 'png', 'jpg').
        """
        plt.figure()
        plt.plot(self.x_data, self.y_data, label=self.title)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        
        # Apply the formatters if set
        if self.x_formatter:
            plt.gca().xaxis.set_major_formatter(self.x_formatter)
        if self.y_formatter:
            plt.gca().yaxis.set_major_formatter(self.y_formatter)

        plt.legend()
        plt.grid(True)
        plt.savefig(filename, format=format)
        plt.close()
