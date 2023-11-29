import math

class ProbabilityCalculator:
    def __init__(self, success_probability):
        if not 0 <= success_probability <= 1:
            raise ValueError("Success probability must be between 0 and 1")
        self.success_probability = success_probability

    def calculate_trials_needed(self, target_probability):
        # Validate the target probability
        if not 0 < target_probability <= 1:
            raise ValueError("Target probability must be greater than 0 and less than or equal to 1")
        # Handle edge cases where success is always guaranteed or impossible
        if self.success_probability in [0, 1]:
            return 1 if self.success_probability == 1 else float('inf')

        # Use the formula to calculate the number of trials needed
        return math.ceil(math.log(1 - target_probability) / math.log(1 - self.success_probability))

    def calculate_probability(self, number_of_trials):
        if number_of_trials < 0:
            raise ValueError("Number of trials must be non-negative")
        
        # Handle edge cases where success is always guaranteed or impossible
        if self.success_probability in [0, 1]:
            return float(self.success_probability)

        success_prob = self.success_probability
        
        # Calculate the probability of at least one success in the given number of trials
        return 1 - (1 - success_prob) ** number_of_trials
