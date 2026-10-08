import pandas as pd
import numpy as np
data = pd.read_csv("day02_usage.csv")
chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()
print("Length:", len(chat))
print("\n Part B")
print("Chat total:", chat.sum())
print("Chat average:", round(chat.mean(), 1))
print("Video total:", video.sum())
print("Video average:", round(video.mean(), 1))
print("Study total:", study.sum())
print("Study average:", round(study.mean(), 1))
print("Games total:", games.sum())
print("Games average:", round(games.mean(), 1))
print("\nPart C")
difference = study - games
best_position = difference.argmax()
worst_position = difference.argmin()
print("Best day:", best_position + 1)
print("Worst day:", worst_position + 1)
print("\nPart D1")
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
print("\nPart D2 ")
daily_total = chat + video + study + games
chat_share = chat / daily_total * 100
video_share = video / daily_total * 100
study_share = study / daily_total * 100
games_share = games / daily_total * 100
print("Chat share:", chat_share)
print("Video share:", video_share)
print("Study share:", study_share)
print("Games share:", games_share)