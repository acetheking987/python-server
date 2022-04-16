def main():
    import json
    import random

    data = {"losses": 0,
            "wins": 0,
            "numbers": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0},
            "win rate": "0%"}

    for i in range(50000000):
        if i % 1000000 == 0:
            print(i)
        random_number = random.randint(1, 6)
        data["numbers"][random_number] += 1
        if random_number == 6:
            data["wins"] += 1
        else:
            data["losses"] += 1

    data["win rate"] = str(round(data["wins"] / (data["wins"] + data["losses"]) * 100, 2)) + "%"
    
    with open("output.json", "w") as f:
        json.dump(data, f)
