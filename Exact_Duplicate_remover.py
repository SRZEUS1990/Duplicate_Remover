def find_duplicates(file_path):
    lines = []
    duplicates = set()
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line in lines:
                duplicates.add(line)
            else:
                lines.append(line)

    for line in lines:
        if line in duplicates:
            print(f"Duplicate: {line}")
        else:
            print(f"Original: {line}")

    # Create a new file with unique lines while preserving order
    unique_file_path = 'unique_' + file_path
    with open(file_path, 'r') as file, open(unique_file_path, 'w') as unique_file:
        unique_lines = set()
        for line in file:
            line = line.strip()
            if line not in unique_lines:
                unique_file.write(line + '\n')
                unique_lines.add(line)
                
    print(f"\nUnique lines saved to: {unique_file_path}")


# Usage: python3 script.py input.txt
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]
find_duplicates(input_file)
