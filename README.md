# world-mental-health-analysis 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Kwangwoon Univ](https://img.shields.io/badge/Kwangwoon_Univ-Business_&_Info_Convergence-red?style=for-the-badge)

---
## 📌 Project Overview

Mental health disorders have become a significant global health concern, imposing substantial social and economic burdens. This project conducts a comprehensive data-driven analysis of global mental health trends from 1990 to 2019, specifically focusing on the interactions between Anxiety Disorders, Eating Disorders, and Bipolar Disorder. By utilizing Prevalence and DALYs (Disability-Adjusted Life Years) datasets, this research explores how these disorders correlate and predicts their future trajectories using linear regression models.

## 🔍 Key Analysis & Results

### 1. Yearly Trends in Prevalence and DALYs
- Description: Visualized the consistent upward trend in global mental health disorder prevalence over the past 30 years.

- Insight: Confirmed that **Anxiety Disorders** and **Depression** account for the largest proportion of cases, with a parallel rise in Disability-Adjusted Life Years (DALYs) across the global population.

<img width="285" height="190" alt="image" src="https://github.com/user-attachments/assets/1b9d76a7-29a4-4253-9630-b3ad14e63b2a" />
<img width="283" height="189" alt="image" src="https://github.com/user-attachments/assets/c7c46843-52a1-427e-b0d1-948aab9d03d6" />


### 2. Cross-Disorder Correlation Analysis
- Results:
Eating Disorders & Bipolar Disorder: Identified a high correlation coefficient of **0.68**.
Anxiety Disorders & Eating Disorders: Confirmed a significant correlation ranging from **0.59 to 0.60**.
Significance: Statistically demonstrated that specific mental disorders are closely interrelated rather than occurring in isolation, highlighting the critical need for multidisciplinary and integrated treatment strategies.

<img width="284" height="213" alt="image" src="https://github.com/user-attachments/assets/ddb1c078-6c06-40af-9ef7-efa86b9916a9" />
<img width="284" height="213" alt="image" src="https://github.com/user-attachments/assets/5387fbfa-87e7-4668-b1f4-20449f989064" />

### 3. Machine Learning-based Future Projections

- Dual-Track Forecasting: We conducted predictive modeling for both **Prevalence** (spread of disorders) and **DALYs** (the actual health burden). This dual approach provides a more holistic view of the future mental health landscape.
- Key Performance (Prevalence):The predictive model for Eating Disorders recorded an **R<sup>2</sup> of 0.9720**, demonstrating exceptional accuracy.Models for Anxiety and Bipolar Disorder also showed consistent upward trends with high reliability.
- Key Performance (DALYs):The DALYs projection models achieved high explanatory power, confirming that the societal burden of mental disorders will rise in tandem with prevalence.This validates the model's utility in predicting not just the number of patients, but the increasing demand for long-term healthcare resources.
## 📊 Visualization: Prevalence vs. DALYs Projections
### 📈 Prevalence Projections (Future Trends in Case Numbers)
<table border="0">
  <tr>
    <td align="center">
      <img width="278" src="https://github.com/user-attachments/assets/003e0601-16df-4612-9376-122bb54db25b" alt="Eating Disorders Prevalence" /><br>
      <b>Bipolar Disorder</b>
    </td>
    <td align="center">
      <img width="279" src="https://github.com/user-attachments/assets/91c838fa-d00a-4d20-a2f6-0a3be56118be" alt="Anxiety Disorders Prevalence" /><br>
      <b>Eating Disorders</b>
    </td>
    <td align="center">
      <img width="279" src="https://github.com/user-attachments/assets/932ca2dd-aabd-4e6b-af4e-f20c464fb298" alt="Bipolar Disorder Prevalence" /><br>
      <b>Anxiety Disorders</b>
    </td>
  </tr>
</table>

#### 📉 DALYs Projections (Future Trends in Health Burden)
<table border="0">
  <tr>
        <td align="center">
      <img width="278" src="https://github.com/user-attachments/assets/c12d8eeb-c0d8-455f-b9e4-81a1e07c7ac9" alt="Anxiety Disorders DALYs" /><br>
      <b>Bipolar Disorder (DALYs)</b>
    </td>
    <td align="center">
      <img width="278" src="https://github.com/user-attachments/assets/dbaa54db-7555-47f9-a037-2337147ca108" alt="Eating Disorders DALYs" /><br>
      <b>Eating Disorders (DALYs)</b>
    </td>
    <td align="center">
      <img width="279" src="https://github.com/user-attachments/assets/5bc3e2b7-add3-4102-91f7-b159c93ec5b1" alt="Bipolar Disorder DALYs" /><br>
      <b>Anxiety Disorders (DALYs)</b>
    </td>
  </tr>
</table>



## 📂 Implementation Details

### 1. Data Preprocessing 
- Missing Value Management: Removed the Code column due to high missing value counts (270 in Prevalence data, 690 in DALYs data) to ensure data integrity.
- Feature Engineering: Simplified long original variable names into clear identifiers such as Schizophrenia, Depression, Anxiety, Bipolar, and Eating_Disorders for better readability and coding efficiency.
- Data Aggregation: Calculated the Yearly Mean for each disorder to minimize noise from regional outliers and capture consistent global trends.

### 2. Research Methodology
- Statistical Distribution Analysis: Utilized Gini Coefficient and Silhouette Analysis by country to understand data clustering and distribution characteristics, justifying the use of mean values for stable trend analysis.
- Correlation Study: Performed Pearson correlation analysis and visualized results through a Correlation Matrix Heatmap to identify significant co-occurrence patterns between disorders.
- Predictive Modeling: Developed Linear Regression models using yearly average data to forecast future trends, evaluating performance through **R<sup>2</sup>** (Coefficient of Determination) and **MSE** (Mean Squared Error).

## 💡 Key Insights & Implications
### 1. Integrated Care & Multidisciplinary Approach
Pathological Connection: The high statistical correlation between disorders (e.g., Eating Disorders and Bipolar Disorder) suggests the likelihood of shared underlying pathological mechanisms.

Integrated Treatment Model: These findings emphasize the necessity of adopting multidisciplinary integrated treatment models that look beyond individual diagnoses to address co-occurring symptoms effectively.

### 2. Preemptive Public Health Policy
Rising Healthcare Demand: The upward trajectory predicted by linear regression analysis signals a significant surge in global demand for mental health services in the coming years.

Evidence-Based Strategy: Governments and health organizations must utilize these predictive insights to prioritize the preemptive allocation of medical resources and establish robust early intervention systems.

## 🛠 Tech Stack

- Language: Python 3.x
- Data Processing: Pandas, NumPy
- Visualization: Matplotlib, Seaborn (Heatmaps, Time-series plots)
- Machine Learning: Scikit-learn (Linear Regression)

## 📚 References
Kaggle: Mental Health Dataset
Here to Help:
The Overlap Between Anxiety and Eating Disorders
Bipolar Disorder
Academic Journals:
Yakovleva et al. (2023): Prevalence of Eating Disorders in Patients with Bipolar Disorder: A Scoping Review of the Literature
McAulay et al. (2019): Eating disorders, bipolar disorders and other mood disorders: Complex and under-researched relationships
Craba et al. (2021): Emerging Trends in Drugs, Addictions, and Health



