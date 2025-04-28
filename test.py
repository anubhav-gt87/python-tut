# write a python function that takes a string and returns the string with all vowels removed

def remove_vowels(input_string):
    """
    This function takes a string and returns the string with all vowels removed.
    
    :param input_string: The input string from which vowels will be removed.
    :return: A new string with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)


# Example usage:

if __name__ == "__main__":
    test_string = "Hello, World!"
    result = remove_vowels(test_string)
    print(f"Original string: {test_string}")
    print(f"String without vowels: {result}")
# Output:
# Original string: Hello, World!
# String without vowels: Hll, Wrld!
# This function uses a generator expression to iterate over each character in the input string
# and checks if it is not a vowel. If the character is not a vowel, it is included in the new string.
# The join() method is then used to concatenate all the characters together into a single string.
# This approach is efficient and works for both lowercase and uppercase vowels.
# The function is case-insensitive and will remove both uppercase and lowercase vowels.
