class ProbabilityCalculator:
    def __init__(self, success_probability):
        """
        Initialize a ProbabilityCalculator object with a given success probability.

        :param success_probability: The probability of success for each trial.
        """
        self.success_probability = success_probability

    def calculate_trials_needed(self, target_probability):
        """
        Calculate the number of trials needed to achieve a target cumulative probability.

        :param target_probability: The target cumulative probability.
        :return: The number of trials needed to reach or exceed the target probability.
        """
        p = self.success_probability  # Probability of success on each trial
        k = 1  # Initialize the trial count
        cumulative_probability = 0  # Initialize the cumulative probability

        # Continue adding probabilities until the cumulative probability exceeds the target
        while cumulative_probability < target_probability:
            cumulative_probability += (1 - p) ** (k - 1) * p
            k += 1  # Increment the trial count

        return k  # Return the number of trials needed

    def calculate_probability(self, number_of_trials):
        """
        Calculate the cumulative probability of success after a specified number of trials.

        :param number_of_trials: The number of trials to consider.
        :return: The cumulative probability of success after the given number of trials.
        """
        p = self.success_probability  # Probability of success on each trial

        # Calculate the cumulative probability using the formula
        cumulative_probability = 1 - (1 - p) ** number_of_trials

        return cumulative_probability  # Return the cumulative probability
