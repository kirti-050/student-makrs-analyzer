import numpy as np

marks = np.array([85, 90, 78, 92, 88, 76, 95, 81])

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

high_scores = marks[marks > 85]

print("Scores above 85:")
print(high_scores)

low_scores = marks[marks < 80]

print("Scores below 80:")
print(low_scores)

average = np.mean(marks)

if average >= 85:
    print("Excellent Performance!")
elif average >= 75:
    print("Good Performance.")
else:
    print("Needs Improvement")

