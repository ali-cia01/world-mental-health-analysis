import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def gini(x):
    """Calculate Gini coefficient"""
    x = np.sort(np.array(x))
    n = len(x)
    if n == 0 or np.sum(x) == 0:
        return 0
    return (n + 1 - 2 * np.sum(np.cumsum(x)) / x.sum()) / n

def run_advanced_analysis(df, targets, title):
    """Run Gini coefficient and clustering analysis"""
    for col in targets:
        # Gini coefficient by country
        print(f"\nGini coefficient for {col} of {title} by country")
        g_val = df.groupby('Entity')[col].apply(lambda x: gini(x.dropna().values))
        print(g_val.sort_values(ascending=False))
        
        # K-Means clustering
        pivot = df.pivot_table(index='Entity', columns='Year', values=col).fillna(0)
        
        if not pivot.empty:
            kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(pivot)
            score = silhouette_score(pivot, kmeans.labels_)
            print(f"Silhouette Score for {col}: {score:.4f}")
