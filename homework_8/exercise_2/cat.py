import sys

def cat(input_file: str) -> None:
    f = open(input_file, 'r')
    print(f.read())


if __name__=='__main__':
    output = cat(sys.argv[1])