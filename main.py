from NumberFormatter import NumberFormatter
from LineChart import LineChart
from ProbabilityCalculator import ProbabilityCalculator

class ChartGenerator:
    def __init__(self, success_probability, start_percentage, end_percentage, custom_calculation=lambda p: p):
        self.validate_percentages(start_percentage, end_percentage)
        self.formatter = NumberFormatter()
        self.prob_calculator = ProbabilityCalculator(success_probability / 100)
         # Create a list of target probabilities
        self.target_probabilities = [i / 100 for i in range(start_percentage, end_percentage)]
        self.custom_calculation = custom_calculation

    @staticmethod
    def validate_percentages(start_percentage, end_percentage):
        if not 1 <= start_percentage < end_percentage:
            raise ValueError("start_percentage must be between 1 and less than end_percentage")
        if not start_percentage + 1 <= end_percentage <= 100:
            raise ValueError("end_percentage must be greater than start_percentage and less than or equal to 100")

    def _calculate_trials(self):
        # Calculate trials needed (or other value using custom calculation logic) for each target probability
        return [self.custom_calculation(self.prob_calculator.calculate_trials_needed(p)) for p in self.target_probabilities]

    def generate_chart(self, title, x_label, y_label, file_name):
        trials_needed = self._calculate_trials()
        chart = LineChart(title=title, x_label=x_label, y_label=y_label)
        chart.add_data(trials_needed, self.target_probabilities)
        chart.set_x_formatter(lambda value, tick: self.formatter.add_commas(value)) 
        chart.set_y_formatter(lambda value, tick: self.formatter.add_percentage(value, 0)) 
        chart.save_chart(file_name, format='png')

def main():
    # custom calculation lambda function to convert the trails need to gems needed
    custom_lambda = lambda p: p / 6 * 250
    chart_generator = ChartGenerator(5, 1, 100, custom_lambda)
    chart_generator.generate_chart("Eatventure Ultimate", "Gems Needed", "Target Probability", "Eatventure_Ultimate_Probability_Chart.png")

if __name__ == "__main__":
    main()
