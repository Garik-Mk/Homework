import sys

def decrep(input_file: str, output_file: str) -> None:
    f = open(input_file, 'r')
    text = f.read()
    for i in range(10):
        text = text.replace(str(i), 'X')
    f.close()
    f = open(output_file, 'w')
    f.write(text)


if __name__=='__main__':
    output = decrep(sys.argv[1], sys.argv[2])