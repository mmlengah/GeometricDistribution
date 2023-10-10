class ProbabilityCalculator:
    def __init__(self, success_probability):
        self.success_probability = success_probability

    def calculate_trials_needed(self, target_probability):
        p = self.success_probability
        k = 1
        cumulative_probability = 0

        while cumulative_probability < target_probability:
            cumulative_probability += (1 - p) ** (k - 1) * p
            k += 1

        return k
    
    def calculate_probability(self, number_of_trials):
        p = self.success_probability
        return 1 - (1 - p) ** number_of_trials