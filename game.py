with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

# Extract placeholders (without < > and in order)
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word + 1:i]  # remove < >
        if word not in words:
            words.append(word)
        start_of_word = -1

# Ask user for inputs
answers = {}

for word in words:
    user_input = input(f"Enter a {word}: ")
    answers[word] = user_input

# Replace placeholders in story
for word in words:
    story = story.replace(f"<{word}>", answers[word])

print(story)