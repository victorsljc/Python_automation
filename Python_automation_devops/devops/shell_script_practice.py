import subprocess

def run_shell():
    subprocess.run(['dir'], shell=True)
    shell_script="e"
    subprocess.run(shell_script,shell=True)

def test_run():
    run_shell()

