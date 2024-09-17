# Since the file 'input.txt' is not provided, I'll write a Python function that could be used to process such a file.
# The function will read the file, parse each line, and perform the required checks.

def process_file(file_path):
    count = 0  # Count of lines meeting the criteria

    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            
            # Count the occurrence of each number
            num_counts = {}
            for num in numbers:
                if num in num_counts:
                    num_counts[num] += 1
                else:
                    num_counts[num] = 1

            # Separate repeated and unique numbers
            repeated_numbers = []
            unique_numbers = []
            for num, count in num_counts.items():
                if count == 2:
                    repeated_numbers.extend([num, num])  # Add the number twice as it's repeated
                elif count == 1:
                    unique_numbers.append(num)

            # Check the criteria
            if len(repeated_numbers) == 2 and unique_numbers:  # Ensure there are unique numbers to avoid division by zero
                avg_repeated = sum(repeated_numbers) / len(repeated_numbers)
                avg_unique = sum(unique_numbers) / len(unique_numbers)
                if avg_repeated < avg_unique:
                    count += 1

    return count

# The function can be used by providing the path to 'input.txt' file. 
# Since the file is not available, I cannot run this code. 
# You can run this code on your system by providing the file path to the 'process_file' pfunction.
print(process_file('input.txt'))