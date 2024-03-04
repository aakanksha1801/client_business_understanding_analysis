from sklearn.cluster import KMeans

# Select relevant features for clustering
features = ['feature1', 'feature2', ...]  # Replace with actual feature names

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)  # Assuming 3 clusters
clients_df['cluster'] = kmeans.fit_predict(clients_df[features])

# Visualize clusters
sns.scatterplot(data=clients_df, x='feature1', y='feature2', hue='cluster')
plt.show()
