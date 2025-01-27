# Strings in Python

# String can be created by enclosing characters inside single quotes, double quotes, or triple quotes. 
# Triple quotes are generally used for multiline strings and docstrings.

# String with Single Quotes
print('Hello, World!')  # Output: Hello, World!

# String with Double Quotes
print("Hello, World!")  # Output: Hello, World!

# Both single quotes and double quotes can be used to create strings in Python, and they are functionally identical.

# String with Triple Quotes
print('''Hello, World!''')  # Output: Hello, World!
print("""Hello, World!""")  # Output: Hello, World!

# Triple quotes allow strings to span multiple lines
print("""This is a 
multiline string.
It spans several lines.""")
# Output:
# This is a 
# multiline string.
# It spans several lines.

# Numbers can also be represented as strings, and their type will be <class 'str'>
print("01234")  # Output: 01234
print(type("01234"))  # Output: <class 'str'>