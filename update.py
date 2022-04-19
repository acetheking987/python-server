from github import Github
from importlib import reload
import main
from time import sleep as sl

########################################################################################################################

G = Github(open("key.txt", "r").read())     #github key

########################################################################################################################

def update():       #update main script
    print("updating")
    repo = G.get_repo("acetheking987/python-server")
    content = repo.get_contents("main.py")
    open("main.py", "wb").write(content.decoded_content)
    sl(5)
    reload(main)
    main.main()