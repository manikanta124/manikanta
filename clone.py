import os
import subprocess

def execute_shell_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out,error)
    pipe.wait()


def git_clone(repo_url):
    cmd = 'git clone ' + repo_url
    execute_shell_command(cmd)


def git_pull():
    cmd='git pull origin master'
    execute_shell_command(cmd)

s1=" https://github.com/mpigelati/Python_adb"


if os.path.isdir("Python_adb"):
    print("file exists")
    os.chdir("C:/Users/barrambelly/PycharmProjects/giit/Python_adb")
    git_pull()
else:
    print("does not exist")
    git_clone(s1)
    os.chdir("C:/Users/barrambelly/PycharmProjects/giit/Python_adb")

s="git log >test.txt"
execute_shell_command(s)
#manikanta

