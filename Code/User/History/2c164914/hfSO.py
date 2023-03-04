import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")
print(df.to_string())
a = [i for i in range(1,57)]
fix, ax = plt.subplots()
ax.plot(df['time'], df['lap'])
plt.show()