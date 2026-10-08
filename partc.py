import pandas as pd
import numpy as np

data = pd.read_csv("day02_usage.csv")

chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()

difference = study - games

best_position = difference.argmax()
worst_position = difference.argmin()

print("Best day:", best_position + 1)
print("Worst day:", worst_position + 1)