#!/usr/local/bin/python
from github import Github
from github import GithubException
import sys

def is_path_in_repo(repo,path):
    try:
        repo.get_contents(path)
        print("Found %s in repository %s"%(path,repo.name))
        return True
    except GithubException:
        print("%s not found in repository %s"%(path,repo.name))
        return False  

g = Github()
repo = g.get_repo(sys.argv[1])

assert(is_path_in_repo(repo,"CITATION.json") or is_path_in_repo(repo,"codemeta.json"))


