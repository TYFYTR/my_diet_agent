import json

try:
    with open("test.json", "r") as file:
        data = json.load(file)
    print("Loaded JSON:", data)
except Exception as e:
    print("Error loading JSON:", e)
  