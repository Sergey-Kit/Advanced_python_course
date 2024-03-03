import sys

def tail(file, lines=10, header=None):
    if header:
        print(header)
    try:
        with open(file, 'r') if file != sys.stdin else file as f:
            all_lines = f.readlines()
            for line in all_lines[-lines:]:
                print(line, end='')
    except FileNotFoundError:
        print(f"Файл {file} не найден", file=sys.stderr)

def main():
    files = sys.argv[1:]
    
    if files:
        for i, file_name in enumerate(files):
            header = f"==> {file_name} <==" if len(files) > 1 else None
            tail(file_name, 10, header)
            if i < len(files) - 1:
                print()
    else:
        tail(sys.stdin, 17)

if __name__ == "__main__":
    main()
