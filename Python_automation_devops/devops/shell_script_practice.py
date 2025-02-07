import subprocess

subprocess.run(['ls','-l'])
shell_script="echo Get year"
subprocess.run(shell_script,shell=True)


