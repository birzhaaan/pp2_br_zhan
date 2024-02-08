from itertools import permutations

def print_permutations(input_str):
    # Generate all permutations of the input string
    perms = permutations(input_str)

    # Print each permutation
    for perm in perms:
        print(''.join(perm))

# Example usage
user_input = input("Enter a string: ")
print_permutations(user_input)