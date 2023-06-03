def analyze_file(file_path):
    line_count = 0
    empty_line_count = 0
    lines_with_z_count = 0
    total_z_count = 0
    lines_with_and_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            line = line.strip()

            if line == "":
                empty_line_count += 1

            if "z" in line:
                lines_with_z_count += 1
                total_z_count += line.count("z")

            if "and" in line:
                lines_with_and_count += 1

    print("Statistics for file:", file_path)
    print("1. Line count:", line_count)
    print("2. Empty line count:", empty_line_count)
    print("3. Lines with 'z':", lines_with_z_count)
    print("4. Total 'z' count:", total_z_count)
    print("5. Lines with 'and':", lines_with_and_count)


def main():
    while True:
        file_path = input("Enter the path to the file (or 'q' to quit): ")

        if file_path.lower() == 'q':
            break

        analyze_file(file_path)

        choice = input("Do you want to analyze another file? (y/n): ")
        if choice.lower() != 'y':
            break


if __name__ == "__main__":
    main()
