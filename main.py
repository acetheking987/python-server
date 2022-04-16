from github import Github
from importlib import reload
from time import sleep as sl
import programme
import datetime
import time

G = Github("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")

def main():
    while True:
        try:
            repo = G.get_repo("acetheking987/python-server")
            content = repo.get_contents("code.py")
            open("programme.py", "wb").write(content.decoded_content)
            sl(5)
            reload(programme)
            start = time.time()
            programme.main()
            end = time.time()
            file = f"{datetime.datetime.now().strftime('%d/%m/output %H:%M:%S')}.json"
            repo.create_file(file, f"took {round(end - start, 3)}s to complete", open("output.json", "r").read())
            print(f"took {round(end - start, 3)}s to complete")

        except Exception as e:
            file = f"error{datetime.datetime.now().strftime('%d/%m/%H:%M:%S')}.md"
            repo.create_file(file, "created new error file", e)
            print("error")
            pass
    
if __name__ == '__main__':
    main()