def main():
    import datetime
    words = open("words.txt", "r").read().split("\n")
    date = str(datetime.datetime.strptime("19/04/22", "%d/%m/%y")).split(" ")[0]
    for word in words:
        if word.split("|")[0] == date:
            return(f"{word.split('|')[1]}", "wordle.md")
