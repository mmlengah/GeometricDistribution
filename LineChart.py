import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define a class for creating line charts
class LineChart:
    def __init__(self, title="", x_label="", y_label=""):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.data = []  # List to store data points as (x, y) tuples
        self.x_formatter = None
        self.y_formatter = None

    def add_data(self, x_values, y_values):
        if isinstance(x_values, list) and isinstance(y_values, list):
            if len(x_values) != len(y_values):
                raise ValueError("Length of x_values and y_values must be the same")
            self.data.extend(zip(x_values, y_values))
        else:
            self.data.append((x_values, y_values))

    def set_title(self, title):
        self.title = title

    def set_x_label(self, x_label):
        self.x_label = x_label

    def set_y_label(self, y_label):
        self.y_label = y_label

    def set_x_formatter(self, func):
        self.x_formatter = FuncFormatter(func)

    def set_y_formatter(self, func):
        self.y_formatter = FuncFormatter(func)

    def save_chart(self, filename, format='png'):
        plt.figure()
        x_data, y_data = zip(*self.data)  # Unpack the data points
        plt.plot(x_data, y_data, label=self.title)
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
