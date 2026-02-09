def check_missing_values(df, data_name):
    """Check and print missing values"""
    print(f"\nMissing values - {data_name}")
    print(df.isnull().sum())
    
def clean_data(df):
    """Remove Code column and drop NA values"""
    df = df.drop(columns=['Code'], errors='ignore').dropna()
    return df

def print_basic_stats(df, targets, data_name):
    """Print basic statistics"""
    print(f"\n{data_name}statistics:")
    print(df[targets].describe())
