import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_yearly_trends(df, targets, title):
    """Plot yearly average trends"""
    plt.figure(figsize=(10, 5))
    df.groupby('Year')[targets].mean().plot(ax=plt.gca())
    plt.title(f'{title}: Yearly Average Trends')
    plt.show()

def plot_boxplot_with_strips(df, targets, title, ylabel):
    """Create boxplot with strip plot overlay"""
    plt.figure(figsize=(12, 6))
    
    sns.boxplot(data=df[targets], whis=np.inf, color="white", showfliers=False)
    sns.stripplot(data=df[targets], alpha=0.2, jitter=True, size=2, palette='Set2')
    
    plt.title(f'{title}: Variability and Individual Observations by Mental Disorders')
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

def plot_country_distribution(df, targets, data_name, point_color, y_label):
    """Plot country-wise distribution for each disease"""
    print(f"\n{'='*30} {data_name} statrting data analysis {'='*30}")
    
    for disease in targets:
        plt.figure(figsize=(20, 7))
        
        sns.boxplot(data=df, x='Entity', y=disease,
                    color='white', whis=np.inf, showfliers=False)
        sns.stripplot(data=df, x='Entity', y=disease,
                      alpha=0.4, jitter=True, size=3, color=point_color)
        
        plt.xticks(rotation=90, fontsize=8)
        plt.title(f'Country-wise Distribution: {data_name} - {disease}', fontsize=16)
        plt.ylabel(y_label, fontsize=12)
        plt.xlabel('Country (Entity)', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.3)
        
        plt.tight_layout()
        plt.show()
