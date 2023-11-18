from NumberFormatter import NumberFormatter
from LineChart import LineChart
from ProbabilityCalculator import ProbabilityCalculator

def generate_chart(success_probability, start_percentage, end_percentage, title, x_label, y_label, file_name, custom_calculation=lambda p: p):
    # Data validation
    if not 1 <= start_percentage < end_percentage:
        raise ValueError("start_percentage must be between 1 and less than end_percentage")

    if not start_percentage + 1 <= end_percentage <= 100:
        raise ValueError("end_percentage must be greater than start_percentage and less than or equal to 100")

    formatter = NumberFormatter()
    probCalculator = ProbabilityCalculator(success_probability / 100)
    targetProbabilities = [i / 100 for i in range(start_percentage, end_percentage + 1)]

    # Apply custom calculation
    trialsNeeded = [custom_calculation(probCalculator.calculate_trials_needed(p)) for p in targetProbabilities]

    chart = LineChart(title=title, x_label=x_label, y_label=y_label)
    chart.add_data(trialsNeeded, targetProbabilities)
    chart.set_x_formatter(lambda v, t: formatter.add_comma(v))
    chart.set_y_formatter(lambda v, t: formatter.convert_to_percentage(v, 0))
    chart.save_chart(file_name, format='png')

def main_app():
     # custom lambda to convert the trails needed to the number of gems needed (based on a loot box with 6 items and a cost of 250 gems each)
    custom_lambda = lambda p: p / 6 * 250

    generate_chart(5, 1, 99, "Eatventure Ultimate", "Gems Needed", "Target Probability", "Eatventure_Ultimate_Probability_Chart.png", custom_lambda)

if __name__ == "__main__":
    main_app()