word = "python"
display = ["_"] * len(word)

while "_" in display:
    letter = input("Guess a letter: ")

    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter

    print(" ".join(display))

print("🎉 You guessed the word:", word)
