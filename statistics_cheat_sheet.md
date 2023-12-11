# Augmented Dickey-Fuller test
We can use the Augmented Dickey-Fuller test to check if the time series is stationary.
In this test:
  - Ho (Null Hypothesis): The time series data is non-stationary
  - H1 (alternate Hypothesis): The time series data is stationary

Assume alpha = 0.05, meaning (95% confidence).
The test results are interpreted with a p-value:
  - if p > 0.05 **FAILS** to reject the null hypothesis (assumes the presence of unit root),
  - if p <= 0.05 reject the null hypothesis.
