import numpy as np

students = np.array([
    [85, 90, 78],
    [92, 88, 76], 
    [95, 81, 89]
])

print("SUbjects wise average:", np.mean(students, axis = 0))

print("Student wise average:", np.mean(students, axis = 1))

print("Highest score in the class:", np.max(students))

print("All scores above 90:", students[students > 90])

