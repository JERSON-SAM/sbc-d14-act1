# Get user input for the main string and the target string
user_input = input("Enter a string: ")
target = input("Enter the target string: ")

# Initialize indices
start_index = user_input.find(target)

# Check if the target is found and calculate the end index
if start_index != -1:
    end_index = start_index + len(target) - 1
    print(f"The word '{target}' is in index {start_index} until {end_index}")
else:
    print(f"The word '{target}' is not found.")

