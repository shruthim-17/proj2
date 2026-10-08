import pandas as pd
import numpy as np

data = pd.read_csv("day02_usage.csv")

chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()

print(chat.sum())
print(round(chat.mean(), 1))

print(video.sum())
print(round(video.mean(), 1))

print(study.sum())
print(round(study.mean(), 1))

print(games.sum())
print(round(games.mean(), 1))