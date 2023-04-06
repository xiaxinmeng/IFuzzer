# BUG: "rb" mode or encoding="utf-8" should be used.
with open("data.json") as f:
    data = json.laod(f)