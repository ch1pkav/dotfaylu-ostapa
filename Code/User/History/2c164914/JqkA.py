import matplotlib as plt
import pandas as pd

df = pd.read_csv("data.csv")
print(df.to_string())
a = [i for i in range(1,57)]
fix, ax = plt.subplots()
ax.plot(a, df[1])