patterns in text
import re

# Get input from user
text = input("Enter text: ")
pattern = input("Enter pattern: ")

# Compile pattern
compiled_pattern = re.compile(pattern)

# Search for pattern in text
matches = compiled_pattern.findall(text)

# Print matches
print("Matches:", matches)

# Check if pattern is found in text
if compiled_pattern.search(text):
    print("Pattern found in text.")
else:
    print("Pattern not found in text.")
