import os
import subprocess

"""def execute_shell_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out,error)
    pipe.wait()

def git_clone(repo_url, repo_dir):
    cmd = 'git clone ' + repo_url + ' ' + repo_dir
    execute_shell_command(cmd, repo_dir)
s1=" https://github.com/mpigelati/Python_adb"
s2="/Users/machalla/Documents/cloneee/cloning"
git_clone(s1,s2)
"""
file="M-adb"
my_file = "/Users/machalla/Documents/cloneee/cloning"
if file in my_file:
    print("file exists")
else:
    print("not exist")




"""def log(s):
    pipe = subprocess.Popen(s, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out, error)
    pipe.wait()
s="git log >log.txt"
log(s)
"""
