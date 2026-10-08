import pandas as pd
import numpy as np

data = pd.read_csv("day02_usage.csv")

chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()
for i in range(30):
    values = [chat[i], video[i], study[i], games[i]]

    winner = np.argmax(values)

    if winner == 0:
        print("Day", i + 1, "Chat")
    elif winner == 1:
        print("Day", i + 1, "Video")
    elif winner == 2:
        print("Day", i + 1, "Study")
    else:
        print("Day", i + 1, "Games")