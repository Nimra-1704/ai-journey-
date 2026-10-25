import matplotlib.pyplot as plt

labels = ["A", "T", "C", "G"]
counts = [10, 15, 8, 12]

plt.bar(labels, counts)
plt.title("Nucleotide Frequency")
plt.savefig("test_chart.png")
print("Chart saved!")