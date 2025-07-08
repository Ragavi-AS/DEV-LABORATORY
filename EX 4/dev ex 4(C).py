import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Seaborn Visualization Examples using Iris Dataset', fontsize=16)

sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', ax=axes[0, 0])
axes[0, 0].set_title('Scatter Plot: Sepal Length vs Sepal Width')

sns.barplot(data=iris, x='species', y='petal_length', ax=axes[0, 1])
axes[0, 1].set_title('Bar Plot: Average Petal Length by Species')

sns.lineplot(data=iris, x=iris.index, y='sepal_length', hue='species', ax=axes[1, 0])
axes[1, 0].set_title('Line Plot: Sepal Length Across Samples')

corr = iris.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1, 1])
axes[1, 1].set_title('Heatmap: Feature Correlation')

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()
