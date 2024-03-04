# Summarize key findings and insights
cluster_means = clients_df.groupby('cluster').mean()
print(cluster_means)
