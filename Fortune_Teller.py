"""Author: Ajinkya Wani
Created: 15 Feb 2019
Revised: 22 Feb 2019
Description: This is fortune teller game which tells your fortune."""

import random


print("Welcome to Fortune Teller by Ajinkya Wani")

print("\nWould you mind answering few questions before we start the game?\n"
      "Please note you can type 'quit' anytime to end the game.\n")

print("Here are the hints to answer these questions\n"
      "(1) Noun – person, place or thing, e.g. house\n"
      "(2) Adjective – describes a noun, e.g. happy\n")


def get_teller():
    file = open("input.txt", "r")
    fortune_list = file.read().split("\n")
    file.close()
    return fortune_list


def replace_word(keyword, index, word):
    teller_list = teller[index].split()
    index_of_keyword = teller_list.index(keyword)
    teller_list[index_of_keyword] = word
    teller[index] = " ".join(teller_list)


def get_words():
    prompts_indexes = [i for i in range(0, len(prompts))]
    random.shuffle(prompts_indexes)
    for i in prompts_indexes:
        while True:
            prompts[i][1] = input(prompts[i][0])
            if prompts[i][1] == "quit":
                print("Game ended successfully, Thanks!")
                exit()
            if validate_input(prompts[i][4], prompts[i][1], prompts[i][3], prompts[i][2]):
                break


def validate_input(validate_for, user_word, keyword, index):
    if validate_for == "number":
        if user_word.isdigit():
            prompts[index][1] = user_word
            replace_word(keyword, index, user_word)
            return True
        else:
            print("Please enter valid entry\n")
    if validate_for == "string":
        if not (user_word.isdigit()):
            prompts[index][1] = user_word
            replace_word(keyword, index, user_word)
            return True
        else:
            print("Please enter valid entry\n")


def get_options_list(start_with):
    if start_with % 2 == 0:
        options_list = even_list
    else:
        options_list = odd_list
    return options_list


even_list = [1, 8, 2, 5]
odd_list = [3, 6, 4, 7]


teller = get_teller()

word = ""
prompts = [
    ["Give me an adjective: ", word, 0, "$adjective", "string"],
    ["Give me an adjective: ", word, 1, "$adjective", "string"],
    ["Choose a person in the room: ", word, 2, "$person", "string"],
    ["Choose a part of the body: ", word, 3, "$body_part", "string"],
    ["Choose an article of clothing you are wearing: ", word, 4, "$clothing_article.", "string"],
    ["Give me an adjective: ", word, 5, "$adjective.", "string"],
    ["Give an adjective: ", word, 6, "$adjective", "string"],
    ["Give me a singular noun: ", word, 6, "$singular_noun.", "string"],
    ["Choose a number greater than one: ", word, 7, "$number_greater_than_one", "number"],
    ["Give me a plural noun: ", word, 7, "$plural_noun", "string"],

]

get_words()

print("\nThank you! Now you are all set to play the game. ")

print("\nAsk your query to me.\n")

colors = ["BLUE", "RED", "GREEN", "PURPLE"]

while True:
    play_game = input("Do you want to continue play the game? Type 'yes' to play or 'no' to exit from the game: ")
    if play_game.upper() == "YES":
        while True:
            print()
            for color in colors:
                print(color, end=", ")
            color_choice = input("\nChoose any one of the colors or type 'quit' to exit the game: ")
            if color_choice.upper() in colors or color_choice == "quit":
                if color_choice == "quit":
                    print("Game ended successfully, thank you for playing!")
                    exit()
                else:
                    start_with = random.randint(0,1)
                    options_list = get_options_list(start_with)

                    chosen_color_list = list(color_choice)
                    for i in range(0, len(chosen_color_list)):
                        print(chosen_color_list[i], end=" ")
                        print(options_list)
                        if i < len(chosen_color_list) - 1:
                            start_with = start_with + 1
                            options_list = get_options_list(start_with)
                    while True:
                        chosen_number = int(input("Choose any number from the list: "))
                        if chosen_number in options_list:
                            print(teller[chosen_number - 1])
                            if chosen_number > 7:
                                chosen_number = chosen_number + 1
                            while True:
                                print("\nWould you mind answering this question again?")
                                new_word = input(prompts[chosen_number - 1][0])
                                if new_word == "quit":
                                    print("Game ended successfully, Thanks!")
                                    exit()
                                if validate_input(prompts[chosen_number - 1][4], new_word,
                                                  prompts[chosen_number - 1][1],
                                                  prompts[chosen_number - 1][2]):
                                    break
                            break
                        else:
                            print("Sorry, the number is not in the list. Please try again!\n")
                    break

            else:
                print("Sorry, the color ain't on the list. Please try again!!\n")

    elif play_game.upper() == "NO":
        print("Thank you for playing! Game ended successfully.")
        exit()

    else:
        print("Please enter either 'yes' or 'no'\n")
