import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("day02_usage.csv")
app_names = ["Chat", "Video", "Study", "Games"]
apps = df[app_names].to_numpy()
days = range(1, len(df) + 1)
plt.figure()
for i, app in enumerate(app_names):
    plt.plot(days, apps[:, i], marker="o", label=app)
plt.show()