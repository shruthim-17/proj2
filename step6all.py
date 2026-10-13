import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("day02_usage.csv")
app_names = ["Chat", "Video", "Study", "Games"]
apps = df[app_names].to_numpy()
days = range(1, len(df) + 1)
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o")
plt.title("A")
plt.show()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o", label=app)
plt.title("B")
plt.show()
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o", label=app)
plt.legend(ncol=4, loc="upper center")
plt.title("B2 - Labels and Legend")
plt.show()
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o", label=app)
plt.legend(ncol=4, loc="upper center")
plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.show()
plt.figure()

for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o", label=app)
day_totals = apps.sum(axis=1)
busiest_index = day_totals.argmax()
busiest_day = busiest_index + 1
busiest_app_index = apps[busiest_index].argmax()
plt.legend(ncol=4, loc="upper center")
plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.annotate(
    f"Busiest Day: {busiest_day}",
    xy=(busiest_day, apps[busiest_index, busiest_app_index]),
    xytext=(
        busiest_day,
        apps[busiest_index, busiest_app_index] + apps.max() * 0.15
    ),
    arrowprops={"arrowstyle": "->"}
)
plt.grid(True, alpha=0.3)
plt.show()
