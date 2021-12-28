import sys
import os
import argparse 
import requests
import json
import time

file_path = os.path.join(sys.path[0], 'token.txt')
f = open(file_path, "r")
secret = f.read()

def mkdir():
    print("Provide name for local folder")
    name = input()
    os.system(f"mkdir {name}")
    print(f"Folder created, going into {name}")
    os.chdir(name)

def git_init():
    mkdir()
    print("Github Username: ")
    username = input()
    print("Project dir name")
    proj_name = input()
    print("Provide small description of the project")
    descr = input()
    payload = { 
        "name": f"{proj_name}",
        "description": f"{descr}",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": False,
        "auto_init": False,
        "branch": "main"
        }
    url = f"https://github.com/{username}/{proj_name}.git"
    print("...Creating repo on GitHub...", "\n")
    r = requests.post("https://api.github.com/user/repos", auth=(username,secret), data=json.dumps(payload))
    time.sleep(0.7)
    print("Http ", r.status_code, " code", "\n")
    os.system(f"{descr} > README.md ")
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "initial commit"')
    os.system("git branch -M main")
    os.system(f"git remote add origin {url}")
    os.system("git push -u origin main")

def git_update():
    os.system("git status")
    print("Run git push ? ")
    if input() == "Yes" or input() == "YES" or input=="si" or input=="SI":
        os.system("git add .")
        os.system('git commit -m "update"')
        os.system("git push origin main")
    else:
        print("Exiting...")

def git_pull():
    os.system("git status")
    print("Run git pull ? ")
    if input() == "Yes" or input() == "YES" or input=="si" or input=="SI":
        os.system("git pull origin main")
    else:
        print("Exiting...")

parser = argparse.ArgumentParser(description='Full Automate Git action from CLI')
parser.add_argument('--init', action='store_true', help='Create remote repo on GitHub')
parser.add_argument('--update', action='store_true', help='Update local repo to GitHub')
parser.add_argument('--pull', action='store_true', help='Pull changes from GitHub to local')
args = parser.parse_args()

if args.init == True:
    git_init()
elif args.update == True:
    git_update()
elif args.pull == True:
    git_pull()
else:
    print("Error")