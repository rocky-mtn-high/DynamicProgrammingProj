import sys
import fileinput


def file_import():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        # Use fileinput.input() to handle both stdin and file input
        input_lines = []
        with fileinput.input(files=(input_file_path,)) as f:
            for line in f:
                input_lines.append(line)
            return process_input(input_lines)
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

def test_import(filename):
    with open(filename, "r") as file:
        input_lines = []
        for line in file:
            input_lines.append(line)
        return process_input(input_lines)
    return 0

def process_input(input_lines):
    logs = [int(log) for log in input_lines[1].split()]
    return logs
