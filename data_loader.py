import pandas as pd

def load_data(prev_path, dalys_path):
    """Load prevalence and DALYs datasets"""
    prev_df = pd.read_csv(prev_path)
    dalys_df = pd.read_csv(dalys_path)
    
    rename_rules = {
        'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized': 'Schizophrenia',
        'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized': 'Depression',
        'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized': 'Anxiety',
        'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized': 'Bipolar',
        'Eating disorders (share of population) - Sex: Both - Age: Age-standardized': 'Eating_Disorders',
        'DALYs (rate) - Sex: Both - Age: Age-standardized - Cause: Depressive disorders': 'Depression',
        'DALYs (rate) - Sex: Both - Age: Age-standardized - Cause: Schizophrenia': 'Schizophrenia',
        'DALYs (rate) - Sex: Both - Age: Age-standardized - Cause: Bipolar disorder': 'Bipolar',
        'DALYs (rate) - Sex: Both - Age: Age-standardized - Cause: Eating disorders': 'Eating_Disorders',
        'DALYs (rate) - Sex: Both - Age: Age-standardized - Cause: Anxiety disorders': 'Anxiety'
    }
    
    prev_df = prev_df.rename(columns=rename_rules)
    dalys_df = dalys_df.rename(columns=rename_rules)
    
    return prev_df, dalys_df
