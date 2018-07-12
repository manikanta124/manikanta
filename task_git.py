import subprocess
def exe_cmd(cmd):
    p= subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    print(str(output.decode('ascii')))
exe_cmd("ls")
exe_cmd("git clone https://github.com/mpigelati/Python_adb")
exe_cmd("cd Python_adb")

#exe_cmd("ls")