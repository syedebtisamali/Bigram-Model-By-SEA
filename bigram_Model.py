import random

# Inputs
# Inputing Data from the File (data.txt)
with open("data.txt", "r") as file:
    text =  file.read()
length = 40
start = "the"
Temperature = 0
# Split Text
words = text.split()
start_word = start.split()
model = {}
# Build the model
model = {}
for i in range(len(words)-1):
        current_word = words[i]
        next_word = words[i+1]
        if current_word in model:
            model[current_word].append(next_word)
        else:
            model[current_word] = [next_word]
# Generate new text
start_word = start_word[-1]
length_of_sentence = length
result = [start]
current_word = start.split()[-1]
for i in range (length - 1):
    if current_word in model:
        next_word = random.choice(model[current_word])
        # Add Next word to Result
        result.append(" " + next_word)
        # Changes the Current Word
        current_word = next_word
    else:
        break
# Print the Generated Text
print("".join(result))