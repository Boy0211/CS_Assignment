import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("istherecorrelation.csv", delimiter=';', decimal=',')

fig, ax = plt.subplots()

ax.plot(df['Year'], df['WO [x1000]'], color='red', marker='o')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('WO students [x1000]', color='red', fontsize=12)

ax2 = ax.twinx()
ax2.plot(df['Year'], df['NL Beer consumption [x1000 hectoliter]'], color='blue', marker='o')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('NL Beer Consumption [x1000 hectoliter]', color='blue', fontsize=12)

plt.show()
