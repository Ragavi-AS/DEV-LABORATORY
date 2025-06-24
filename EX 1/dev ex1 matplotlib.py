import matplotlib.pyplot as plt

# Sample data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
scores = [85, 92, 78, 90, 88]

# Create a bar chart
plt.bar(students, scores, color='skyblue')

# Add title and labels
plt.title('Student Scores')
plt.xlabel('Students')
plt.ylabel('Scores')

# Show the plot
plt.show()
