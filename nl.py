import sys

def print_numbered_lines(source):
    line_number = 1
    for line in source:
        print(f"{line_number}\t{line}", end='')
        line_number += 1

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        with open(file_name, 'r') as file:
            print_numbered_lines(file)
    else:
        print_numbered_lines(sys.stdin)

if __name__ == "__main__":
    main()