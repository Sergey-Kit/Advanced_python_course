import sys

def count_stats(file):
    lines = words = bytes = 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes += len(line.encode('utf-8'))
    return lines, words, bytes

def print_stats(lines, words, bytes, name=None):
    print(f"{lines} {words} {bytes} {name if name else ''}".strip())

def main():
    total_lines = total_words = total_bytes = 0
    files = sys.argv[1:]

    if files:
        for file_name in files:
            try:
                with open(file_name, 'r') as file:
                    lines, words, bytes = count_stats(file)
                    print_stats(lines, words, bytes, file_name)
                    total_lines += lines
                    total_words += words
                    total_bytes += bytes
            except FileNotFoundError:
                print(f"Файл {file_name} не найден", file=sys.stderr)
        if len(files) > 1:
            print_stats(total_lines, total_words, total_bytes, 'total')
    else:
        lines, words, bytes = count_stats(sys.stdin)
        print_stats(lines, words, bytes)

if __name__ == "__main__":
    main()