from src.data_loader import load_data
from src.preprocessing import check_missing_values, clean_data, print_basic_stats
from src.visualization import plot_yearly_trends, plot_boxplot_with_strips, plot_country_distribution
from src.statistical_analysis import run_correlation, run_regression_trend
from src.advanced_analysis import run_advanced_analysis

# Configuration
PREV_PATH = 'data/mental-illnesses-prevalence.csv'
DALYS_PATH = 'data/updated_burden_data.csv'
TARGETS = ['Schizophrenia', 'Depression', 'Anxiety', 'Bipolar', 'Eating_Disorders']
TREND_TARGETS = ['Anxiety', 'Eating_Disorders', 'Bipolar']

def main():
    # Load data
    prev_df, dalys_df = load_data(PREV_PATH, DALYS_PATH)
    
    # Preprocessing
    check_missing_values(prev_df, "Prevalence")
    check_missing_values(dalys_df, "DALYs")
    
    prev_df = clean_data(prev_df)
    dalys_df = clean_data(dalys_df)
    
    print_basic_stats(prev_df, TARGETS, "Prevalence")
    print_basic_stats(dalys_df, TARGETS, "DALYs")
    
    # Visualization
    plot_yearly_trends(prev_df, TARGETS, "Prevalence")
    plot_yearly_trends(dalys_df, TARGETS, "DALYs")
    
    plot_boxplot_with_strips(prev_df, TARGETS, "Prevalence", "Share of Population (%)")
    plot_boxplot_with_strips(dalys_df, TARGETS, "DALYs", "DALYs Rate")
    
    # Country-wise distribution
    datasets = [
        ('Prevalence', prev_df, 'royalblue', 'Share of Population (%)'),
        ('DALYs', dalys_df, 'indianred', 'DALYs Rate')
    ]
    
    for data_name, df, point_color, y_label in datasets:
        plot_country_distribution(df, TARGETS, data_name, point_color, y_label)
    
    # Statistical analysis
    run_correlation(prev_df, TARGETS, "Prevalence")
    run_correlation(dalys_df, TARGETS, "DALYs")
    
    run_regression_trend(prev_df, TREND_TARGETS, "Prevalence")
    run_regression_trend(dalys_df, TREND_TARGETS, "DALYs")
    
    # Advanced analysis
    run_advanced_analysis(prev_df, TREND_TARGETS, "Prevalence")
    run_advanced_analysis(dalys_df, TREND_TARGETS, "DALYs")

if __name__ == "__main__":
    main()
