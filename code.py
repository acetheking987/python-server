def main():
    import json
    import random

    data = {"losses": 0, "wins": 0, "numbers": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}}

    for i in range(50000):
        random_number = random.randint(1, 6)
        data["numbers"][random_number] += 1
        if random_number == 6:
            data["wins"] += 1
        else:
            data["losses"] += 1
    
    with open("output.json", "w") as f:
        json.dump(data, f)
