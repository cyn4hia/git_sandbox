import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame
data = {'Name': ['John', 'Emma', 'Peter'],
    'Age': [25, 28, 30],
    'City': ['New York', 'London', 'Paris'],
    'Qualification': np.random.randn(3)}



status_data = {'Up/Down': [100, -150, 0],
               'Value': ['Up', 'Down', 'DownRate'],
               'ValueRate': ['UpRate', 'DownRate', '']}

df = pd.DataFrame(data)


labels = df["Name"]
sizes = df["Age"]

for i in range(len(df["Age"])):
    df["Age"][i] = df["Age"][i] + 10

fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)
ax.bar(labels, sizes, color=['tab:red', 'tab:blue','tab:orange'])

plt.show()


# Print the DataFrame
print(df)
