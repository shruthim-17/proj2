import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("day02_usage.csv")

app_names = ["Chat", "Video", "Study", "Games"]
apps = df[app_names].to_numpy()
days = np.arange(1, len(df) + 1)

# Step 5 Part D: Calculate percentages
day_totals = apps.sum(axis=1, keepdims=True)

percentages = np.divide(
    apps,
    day_totals,
    out=np.zeros_like(apps, dtype=float),
    where=day_totals != 0
) * 100

print("Percentage row sums:")
print(np.round(percentages.sum(axis=1), 2))

# Find busiest day
busiest_index = int(np.argmax(day_totals[:, 0]))
busiest_day = int(days[busiest_index])
busiest_total = int(day_totals[busiest_index, 0])

# A — Bad chart
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i])

plt.title("A - The Bad Version")
plt.show()

# B1 — Add labels
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], label=app)

plt.title("B1 - Labels")
plt.show()

# B2 — Add legend
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], label=app)

plt.legend(ncol=4)
plt.title("B2 - Labels and Legend")
plt.show()

# B3 — Add title and axis labels
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], label=app)

plt.legend(ncol=4)
plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.show()

# B4 — Add markers, annotation and gridlines
plt.figure()

for i, app in enumerate(app_names):
    plt.plot(
        days, apps[:, i],
        marker="o", markersize=3,
        label=app
    )

plt.legend(ncol=4)
plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Minutes")

# Find the app with maximum usage on the busiest day
busiest_app_index = int(np.argmax(apps[busiest_index]))

plt.annotate(
    f"Busiest day: {busiest_day}",
    xy=(
        busiest_day,
        apps[busiest_index, busiest_app_index]
    ),
    xytext=(
        busiest_day,
        apps[busiest_index, busiest_app_index]
        + max(5, apps.max() * 0.12)
    ),
    arrowprops={"arrowstyle": "->"},
    ha="center"
)

plt.grid(True, alpha=0.25)
plt.show()

# C — Final figure with two panels
fig, (ax1, ax2) = plt.subplots(
    2, 1,
    figsize=(12, 9),
    sharex=True,
    gridspec_kw={"height_ratios": [2, 1]}
)

# Top panel: Daily usage in minutes
for i, app in enumerate(app_names):
    ax1.plot(
        days, apps[:, i],
        marker="o", markersize=3,
        label=app
    )

ax1.set_title(
    "Daily App Usage: Minutes and Share of Attention"
)
ax1.set_ylabel("Minutes")
ax1.legend(ncol=4)
ax1.grid(True, alpha=0.25)

ax1.annotate(
    f"Busiest day: {busiest_day} "
    f"({busiest_total} total minutes)",
    xy=(
        busiest_day,
        apps[busiest_index, busiest_app_index]
    ),
    xytext=(
        busiest_day,
        apps[busiest_index, busiest_app_index]
        + max(5, apps.max() * 0.15)
    ),
    arrowprops={"arrowstyle": "->"},
    ha="center"
)

# Bottom panel: Stacked percentage bars
bottom = np.zeros(len(df))

for i, app in enumerate(app_names):
    ax2.bar(
        days,
        percentages[:, i],
        bottom=bottom,
        label=app
    )
    bottom += percentages[:, i]

ax2.set_xlabel("Day")
ax2.set_ylabel("Share (%)")
ax2.set_ylim(0, 100)
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.grid(True, axis="y", alpha=0.25)

# D — Save the final chart
plt.tight_layout()
plt.savefig(
    "day02_usage_chart.png",
    dpi=200,
    bbox_inches="tight"
)

print("\nSaved: day02_usage_chart.png")
print(
    f"Busiest day: Day {busiest_day}, "
    f"with {busiest_total} total minutes."
)

plt.show()