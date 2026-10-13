import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
df = pd.read_csv("day02_usage.csv")

Days = df["Day"].to_numpy()
Apps = ["Chat","Video","Study","Games"]
usage = df[Apps].to_numpy()
per_day = usage.sum(axis=1)
shares = usage/per_day[:,None]*100

fig,(ax1,ax2) = plt.subplots(2,1,figsize=(11,8))

for i,app in enumerate(Apps):
    ax1.plot(Days,usage[:,i],marker="o",markersize=3,linewidth=1.6,label=app)

ax1.set_title("Daily Minutes per App - 30 Days")
ax1.set_xlabel("Day")
ax1.set_ylabel("Minutes")
ax1.legend(ncol=4,frameon=False)
peak_day = int(per_day.argmax())
ax1.annotate(f"Busiest Day: {Days[peak_day]}",xy=(Days[peak_day],usage[peak_day].max()),xytext=(Days[peak_day]+3,usage[peak_day].max()+3),arrowprops=dict(arrowstyle="->"))
ax1.grid(alpha=0.3)
fig.savefig("abc.png")
bottom = np.zeros(30)
for i,app in enumerate(Apps):
    bottom += usage[:,i]
    ax2.bar(Days,usage[:,i],bottom=bottom-usage[:,i],label=app)
fig.savefig("abc.png")
bottom = np.zeros(len(Days))
for i,app in enumerate(Apps):
    bottom += shares[:,i]
    ax2.bar(Days,shares[:,i],bottom=bottom-shares[:,i],label=app)
ax2.set_title("Share of each day (%)- every bar total 100%")
ax2.set_xlabel("Day")
ax2.set_ylabel("Share (%)")
ax2.set_ylim(0, 100)
ax2.legend(ncol=4,frameon=False, loc="lower right")
fig.tight_layout()
fig.savefig("abc.png")
fig.savefig("day02_usage.png")
print("saved day02_usage.png")
print("panel 2 sanity check - each bar should total 100%")
print(shares.sum(axis=1))


