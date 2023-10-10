# GeometricDistribution
Using python to calculate geometric distribution

# Probability Calculator

## Introduction
The ProbabilityCalculator class is designed to assist in probability calculations for Bernoulli trials. It has methods to estimate the number of trials needed to achieve a target probability of at least one success, and to calculate the probability of at least one success in a given number of trials.

## Methods 
### __init__(self, success_probability)
Initialises the ProbabilityCalculator class.

#### Parameters
success_probability: The probability of success of at least a single event. Must be between 0 and 1.

### calculate_trials_needed(self, target_probability)
Calculates the minimum number of trails needed to achieve the target probability.

#### Parameters
target_probability: The target probability of at least one success. Must be between 0 and 1.

#### Returns
int: The minimum number of trails needed.

### calculate_probability(self, number_of_trials)
Calculates the probability of achieving one success in a specified number of trials.

#### Parameters
number_of_trails: The number of trails to be conducted.

#### Returns
float: The calculated probability of at least one success.