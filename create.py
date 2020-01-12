import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("username")
password = os.getenv("password")
path = "/Users/harisbeslic/Documents/Projects/"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
