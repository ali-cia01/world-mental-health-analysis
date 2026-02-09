import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_correlation(df, targets, title):
    """Calculate and visualize correlation matrix"""
    corr = df[targets].corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'Correlation Matrix: {title}')
    plt.show()
    
    return corr

def run_regression_trend(df, targets, title):
    """Run linear regression and predict future trends"""
    print(f"\n--- {title} Trend Forecasting Analysis ---")
    yearly_avg = df.groupby('Year')[targets].mean().reset_index()
    
    for col in targets:
        X = yearly_avg[['Year']]
        y = yearly_avg[col]
        
        model = LinearRegression().fit(X, y)
        preds = model.predict(X)
        
        r2 = r2_score(y, preds)
        mse = mean_squared_error(y, preds)
        print(f"[{col}] R²: {r2:.4f}, MSE: {mse:.4f}")
        
        future = pd.DataFrame({'Year': np.arange(X['Year'].max()+1, X['Year'].max()+11)})
        f_preds = model.predict(future)
        
        plt.figure(figsize=(10, 5))
        plt.scatter(X, y, label='Actual')
        plt.plot(X, preds, color='red', label='Linear Fit')
        plt.plot(future, f_preds, 'g--', label='Future 10y')
        plt.title(f'Trend: {title} - {col}')
        plt.legend()
        plt.show()
