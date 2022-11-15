import sys

def wc(flag: str, path: str) -> int:
    f = open(path, 'r')
    text = f.read()
    if flag == '-c':
        return len(text)
    elif flag == '-w':
        text = text.split(' ')
        return len(text)
    elif flag == '-l':
        lines = text.count('\n')
        return lines
    else: 
        raise ValueError

if __name__=='__main__':
    output = wc(sys.argv[1], sys.argv[2])
    print(output)