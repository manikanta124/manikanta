import subprocess
def execute_shell_command(cmd, work_dir):
    pipe = subprocess.Popen(cmd, shell=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print (out, error)
    pipe.wait()

def git_clone(repo_url, repo_dir):
    cmd = 'git clone ' + repo_url + ' ' + repo_dir
    execute_shell_command(cmd, repo_dir)
s1= "https://github.com/mpigelati/Python_adb"
s2= "/Users/machalla/Documents/clonee"
git_clone(s1,s2)