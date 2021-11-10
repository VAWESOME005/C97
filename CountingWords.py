intro = input("Introduce yourself: ")
character_count = 0
word_count = 1
for i in intro:
    character_count = character_count + 1
    if i == " ":
        word_count = word_count + 1
print("# of Characters: ", character_count)
print("# of Words: ", word_count)

    