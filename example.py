from NumberFormatter import NumberFormatter
from LineChart import LineChart
from ProbabilityCaculator import ProbabilityCalculator

if __name__ == "__main__":
    formatter = NumberFormatter()

    def format_x_as_comma(value, tick_number):
        return formatter.add_comma(value)

    def format_y_as_percentage(value, tick_number):
        return formatter.convert_to_percentage(value, 0)

    probCalculator = ProbabilityCalculator(0.05)
    targetProbabilities = [i/100 for i in range(1, 100)]
    trialsNeeded = [probCalculator.calculate_trials_needed(p) / 6 * 250 for p in targetProbabilities]   

    chart = LineChart(title="Eatventure Ultimate", x_label="Gems Needed", y_label="Target Probability")
    chart.add_data(trialsNeeded, targetProbabilities)   

    chart.set_x_formatter(format_x_as_comma)
    chart.set_y_formatter(format_y_as_percentage)
    
    chart.save_chart("Eatventure_Ultimate_Probability_Chart.png", format='png')  
