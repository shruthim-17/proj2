import pandas as pd
import numpy as np

data = pd.read_csv("day02_usage.csv")

chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()

daily_total = chat + video + study + games

chat_share = chat / daily_total * 100
video_share = video / daily_total * 100
study_share = study / daily_total * 100
games_share = games / daily_total * 100

print(chat_share)
print(video_share)
print(study_share)
print(games_share)