possible_words = []
letter = 'a'
position = 1
word_list = []
with open(r"C:\Users\abhis\OneDrive\Desktop\project\wordle_dictionary.txt") as w:
    possible_words = w.readlines()

print("Follow these steps:")
print("\t1. Make your first guess in wordle")
print("\t2. Provide each letter, color, and position when asked to do so in the program")
print("\t\ty = yellow")
print("\t\tg = green")
print("\t\tb = black")
print("\t3. Make the next guess using the possible word list")
print("\t4. Repeat until you find the word of the day\n")
word_list = possible_words
count11 = 0

while letter != 'quit':
    count11 +=1
    templ = []
    contl = 0

    letter = input("What letter do you know: ")
    color = input("What color is the letter (y, g, b): ")

    # If we got a green letter or yellow letter
    if color == 'g' or color == 'y':
        position = int(input("What position is the letter in (1 - 5): "))
        position -= 1

    # Go through all possible words
    for word in word_list:
        contl +=1 

        # Green
        if color == 'g':
            if word[position] == letter:
                templ.append(word)
                
        # Black
        elif color == 'b':
            if letter not in word:
                templ.append(word)

        # Yellow
        elif color == 'y':
            if letter in word:
                if word[position] != letter:
                    templ.append(word)

    word_list = templ
    if(count11%5==0):
        print(*word_list)
        print(contl)