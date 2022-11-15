import subprocess
import sys
import os

def redir(argument_list: list):
    cmd = argument_list[0]
    for i in range(1, len(argument_list)):
        if argument_list[i] == '-out' or argument_list[i] == '-err':
            break
        else:
            cmd += ' ' + argument_list[i]

    out_index = argument_list.index('-out')
    if argument_list[out_index + 1] == '-a':
        out = argument_list[out_index + 2]
        out_file = open(out, 'w')
    else:
        out = argument_list[out_index + 1]
        if not os.path.isfile(out):
            out_file = open(out, 'w')
        else:
            out_file = open(out, 'a')

    err_index = argument_list.index('-err')
    if argument_list[err_index + 1] == '-a':
        err = argument_list[err_index + 2]
        err_file = open(err, 'w')
    else:
        err = argument_list[err_index + 1]
        if not os.path.isfile(err):
            err_file = open(err, 'w')
        else:
            err_file = open(err, 'a')
    
    subprocess.Popen(cmd.split(' '), stdout=out_file, stderr=err_file)
    




if __name__=='__main__':
    redir(sys.argv[1:])
