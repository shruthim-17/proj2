import pandas as pd
import numpy as np

data = pd.read_csv("day02_usage.csv")

chat = data["Chat"].to_numpy()
video = data["Video"].to_numpy()
study = data["Study"].to_numpy()
games = data["Games"].to_numpy()

print(len(chat))