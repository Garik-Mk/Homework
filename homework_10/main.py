import subprocess

proc = subprocess.Popen(["python3", "/home/v1king/My_own_scripts/Homework/homework_10/polish_notation.py"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.stdin.write(b"+ 3 5\n")
proc.stdin.write(b"* 1 6\n")
proc.stdin.close()

while proc.returncode is None:
    proc.poll()

print ("I am back from the child program this:\n{0}".format(proc.stdout.read()))