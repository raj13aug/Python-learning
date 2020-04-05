import subprocess

completed = subprocess.run(["python3", "other.py"], 
                           capture_output=True,
                           text=True,
                           )
print("args", completed.args)
print("returncode", completed.returncode)
print("stderror", completed.stderr)
print("stdout", completed.stdout)
if completed.returncode != 0:
    print(completed.stderr)
