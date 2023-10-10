# Import necessary classes from modules
from NumberFormatter import NumberFormatter
from LineChart import LineChart
from ProbabilityCaculator import ProbabilityCalculator

if __name__ == "__main__":
    # Create a NumberFormatter object to format numbers
    formatter = NumberFormatter()

    # Define a custom formatter function for the X-axis of the chart
    def format_x_as_comma(value, tick_number):
        """
        Format X-axis tick labels with commas.

        :param value: Tick value to format.
        :param tick_number: Tick number.
        :return: Formatted label as a string.
        """
        return formatter.add_comma(value)

    # Define a custom formatter function for the Y-axis of the chart
    def format_y_as_percentage(value, tick_number):
        """
        Format Y-axis tick labels as percentages.

        :param value: Tick value to format.
        :param tick_number: Tick number.
        :return: Formatted label as a string.
        """
        return formatter.convert_to_percentage(value, 0)

    # Create a ProbabilityCalculator object with a success probability of 5%
    probCalculator = ProbabilityCalculator(0.05)

    # Calculate target probabilities from 1% to 99%
    targetProbabilities = [i/100 for i in range(1, 100)]

    # Calculate the number of trials needed for each target probability
    # and convert it to the number of gems needed (based on a loot box with 6 items and a cost of 250 gems each)
    trialsNeeded = [probCalculator.calculate_trials_needed(p) / 6 * 250 for p in targetProbabilities]

    # Create a LineChart object for visualizing the data
    chart = LineChart(title="Eatventure Ultimate", x_label="Gems Needed", y_label="Target Probability")
    
    # Add the data points to the chart
    chart.add_data(trialsNeeded, targetProbabilities)

    # Set custom formatters for X and Y axes
    chart.set_x_formatter(format_x_as_comma)
    chart.set_y_formatter(format_y_as_percentage)

    # Save the chart as an image file
    chart.save_chart("Eatventure_Ultimate_Probability_Chart.png", format='png')
