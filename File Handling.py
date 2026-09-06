def process_file(input_file, output_file):
    # Create a sample input file
    with open("input.txt", "w") as f:
        f.write("Hello World\n")
        f.write("Python Scripting\n")
        f.write("All student of SY-14 batch B are very obedient and Intelligent.\n")

    # Step 1: Read the input file using a context manager
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Step 2: Count total lines
    total_lines = len(lines)

    # Step 3: Extract the first two lines
    first_two_lines = lines[:2]

    # Step 4: Write extracted data to a new output file
    with open(output_file, 'w') as outfile:
        outfile.write(f"Total Lines Counted: {total_lines}\n")
        outfile.write("First Two Lines:\n")
        outfile.writelines(first_two_lines)

    return total_lines, first_two_lines


if __name__ == "__main__":
    total, first_two = process_file(
        "input.txt", "output.txt"
    )

    print(f"Total lines in file: {total}")
    print("First two lines extracted:")

    for line in first_two:
        print(line.strip())

    print("Data written to output.txt")
