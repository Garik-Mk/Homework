import subprocess

def redir(args):
    cmd_out = args[0]
    cmd_in = args[1]
    proc = subprocess.Popen(cmd_out.split(' '), stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    while proc.returncode is None:
        proc.poll()
    
    subprocess.Popen(cmd_in.split(' ', stdin=proc.stdout.read()))