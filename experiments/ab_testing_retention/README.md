# Customer Retention A/B Testing

## Overview

This project demonstrates an end-to-end A/B testing workflow for evaluating a hypothetical customer-retention campaign. The experiment uses reproducible synthetic data to compare customer churn between a control group and a treatment group receiving a retention offer.

**Important:** All experimental outcomes and financial assumptions are simulated. The results do not represent a real campaign or establish real-world effectiveness.

## Business Question

Would a hypothetical retention offer reduce customer churn sufficiently to justify the cost of a campaign?

## Experimental Design

- **Design:** Two-group randomized experiment (simulated)
- **Sample size:** 10,000 customers
- **Assignment:** Random allocation to control and treatment groups
- **Primary metric:** Customer churn rate
- **Significance level:** 5%
- **Statistical method:** Two-proportion z-test
- **Uncertainty analysis:** 95% confidence intervals

## Key Results

| Metric | Result |
|---|---:|
| Control churn rate | 27.70% |
| Treatment churn rate | 23.75% |
| Absolute churn reduction | 3.95 percentage points |
| Relative churn reduction | 14.25% |
| Z-statistic | -4.513 |
| P-value | Approximately 0.000006 |
| 95% CI for treatment-minus-control difference | -5.66 to -2.23 percentage points |

The simulated experiment rejects the null hypothesis of equal churn rates at the 5% significance level.

## Business Impact Analysis

Under the illustrative financial assumptions used in the notebook:

- Proposed campaign size: 10,000 customers
- Assumed contribution value per retained customer: €400
- Assumed offer cost per customer: €15
- Assumed operating cost per customer: €2
- Estimated net benefit: approximately -€12,174
- Estimated ROI: approximately -7.2%

The illustrative 95% uncertainty range for net benefit is approximately -€80,637 to +€56,290.

These estimates assume that the estimated treatment effect applies to a full rollout and that the specified financial assumptions remain fixed. They are not a forecast of real business performance.

## Tools and Techniques

- Python
- NumPy and pandas
- Matplotlib
- Randomized group assignment
- Binary outcome analysis
- Hypothesis testing
- Confidence intervals
- Business-impact and sensitivity analysis

## Limitations

This is a methodology demonstration using simulated data and assumed treatment effects. A real deployment decision would require a properly conducted experiment, validated business assumptions, and consideration of customer lifetime value, campaign costs, implementation risks, and other relevant outcomes.

## Reproducibility

The notebook uses a fixed random seed so that the simulated dataset and results can be reproduced. Run the notebook cells in order to generate the dataset, statistical analysis, visualization, and financial calculations.