import matplotlib.pyplot as plt
import seaborn as sns

# Summary statistics
print(clients_df.describe())

# Visualize distributions and relationships
sns.pairplot(clients_df)
plt.show()
