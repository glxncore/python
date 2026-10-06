# Store a short paragraph using a multiline string
paragraph = """Python is a programming course designed for beginners.
This Python course teaches the basics of programming, variables, loops,
and functions."""

# Display the length of the paragraph
print("Length of paragraph:", len(paragraph))

# Display the first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Display the first 50 characters
print("Preview:", paragraph[:50])

# Replace all occurrences of "Python" with "PYTHON"
paragraph = paragraph.replace("Python", "PYTHON")
print("After replacement:")
print(paragraph)

# Convert the paragraph to lowercase
paragraph = paragraph.lower()

# Remove extra whitespace from the start and end
paragraph = paragraph.strip()

# Split the paragraph into individual words
words = paragraph.split()
print("List of words:", words)

# Check if the word "course" exists
if "course" in words:
    print("The word 'course' was found in the paragraph.")

# Display the final message using format()
message = "The course description is {} characters long and has {} words.".format(
    len(paragraph), len(words)
)

print(message)