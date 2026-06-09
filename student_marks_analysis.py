import matplotlib.pyplot as plt

names = ["Ali", "Ahmed", "Sara", "Fatima", "Zaid"]
marks = [85, 90, 78, 92, 88]

plt.bar(names, marks)
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()