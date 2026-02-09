# world-mental-health-analysis 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Kwangwoon Univ](https://img.shields.io/badge/Kwangwoon_Univ-Business_&_Info_Convergence-red?style=for-the-badge)

📌 Project Overview

Mental health disorders have become a significant global health concern, imposing substantial social and economic burdens. This project conducts a comprehensive data-driven analysis of global mental health trends from 1990 to 2019, specifically focusing on the interactions between Anxiety Disorders, Eating Disorders, and Bipolar Disorder. By utilizing Prevalence and DALYs (Disability-Adjusted Life Years) datasets, this research explores how these disorders correlate and predicts their future trajectories using linear regression models.

🔍 Key Analysis & Results
1. Yearly Trends in Prevalence and DALYs
Description: Visualized the consistent upward trend in global mental health disorder prevalence over the past 30 years.
Insight: Confirmed that Anxiety Disorders and Depression account for the largest proportion of cases, with a parallel rise in Disability-Adjusted Life Years (DALYs) across the global population.


2. Cross-Disorder Correlation Analysis
Results:
Eating Disorders & Bipolar Disorder: Identified a high correlation coefficient of 0.68.
Anxiety Disorders & Eating Disorders: Confirmed a significant correlation ranging from 0.59 to 0.60.
Significance: Statistically demonstrated that specific mental disorders are closely interrelated rather than occurring in isolation, highlighting the critical need for multidisciplinary and integrated treatment strategies.
3. Machine Learning-based Future Projections
Model: Linear Regression.
Performance: The predictive model for Eating Disorders achieved a high explanatory power with an R<sup>2</sup>  value of 0.97, enabling precise forecasting of potential prevalence increases over the next decade.

🛠 Tech Stack

- Language: Python 3.x
- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn (Heatmaps, Time-series plots)
- Machine Learning: Scikit-learn (Linear Regression)

📂 Implementation Details

1. Data Preprocessing 
- Missing Value Management: Removed the Code column due to high missing value counts (270 in Prevalence data, 690 in DALYs data) to ensure data integrity.
- Feature Engineering: Simplified long original variable names into clear identifiers such as Schizophrenia, Depression, Anxiety, Bipolar, and Eating_Disorders for better readability and coding efficiency.
- Data Aggregation: Calculated the Yearly Mean for each disorder to minimize noise from regional outliers and capture consistent global trends.

2. Research Methodology
- Statistical Distribution Analysis: Utilized Gini Coefficient and Silhouette Analysis by country to understand data clustering and distribution characteristics, justifying the use of mean values for stable trend analysis.
- Correlation Study: Performed Pearson correlation analysis and visualized results through a Correlation Matrix Heatmap to identify significant co-occurrence patterns between disorders.
- Predictive Modeling: Developed Linear Regression models using yearly average data to forecast future trends, evaluating performance through R<sup>2</sup> (Coefficient of Determination) and MSE (Mean Squared Error).




