import matplotlib.pyplot as plt


frequency = {
    5: 1250,
    6: 1250,
    7: 1300,
    8: 1300,
    9: 1250,
    10: 1250
}

new_freq = {}

slope = 2

original_range = frequency.keys()

for i in original_range:
    new_key = 2*i - 7
    print(new_key)
    new_freq[new_key] = frequency[i]

print(new_freq)
plt.bar(frequency.keys(), frequency.values())
plt.bar(new_freq.keys(), new_freq.values())
plt.show()