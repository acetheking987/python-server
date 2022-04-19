from github import Github
from importlib import reload
from time import sleep as sl
import psutil
import programme
import update
import datetime
import time
import json

G = Github(open("key.txt", "r").read())
VERSION = 2.1

def update_check():
    repo = G.get_repo("acetheking987/python-server")
    content = repo.get_contents("version.md")
    if float(content.decoded_content) > VERSION:
        update.update()

def main():
    cycles = 0
    while True:
        cycles += 1
        try:
            update_check()

            repo = G.get_repo("acetheking987/python-server")
            content = repo.get_contents("code.py")
            open("programme.py", "wb").write(content.decoded_content)

            sl(5)
            reload(programme)
        
            start = time.time()
            upload, filename = programme.main()
            end = time.time()

            if upload:
                if filename:
                    try:
                        content = repo.get_contents(upload["filename"])
                        repo.update_file(upload["filename"], f"took {round(end - start, 3)}s to complete", upload["data"], content.sha)

                    except Exception as e:
                        if "404" in str(e):
                            repo.create_file(upload["filename"], f"took {round(end - start, 3)}s to complete", json.dumps(upload["data"]))


                file = f"{datetime.datetime.now().strftime('%d/%m/output %H:%M:%S')}.json"
                repo.create_file(file, f"took {round(end - start, 3)}s to complete", json.dumps(upload))

            print(f"took {round(end - start, 3)}s to complete  |  cycle {cycles}")

            if cycles % 60 == 0:
                content = repo.get_contents("stats.md")
                stats = f"""

                date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
                cycles: {cycles}

                         """

                repo.update_file("stats.md", "updated stats", stats, content.sha)

        except Exception as e:
            try:
                file = f"error{datetime.datetime.now().strftime('%d/%m/%H:%M:%S')}.md"
                repo.create_file(file, "created new error file", e)
                print("error")
                pass

            except:
                sl(60)
                pass

if __name__ == '__main__':
   main()
