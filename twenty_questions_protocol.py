# Twenty Questions Protocol
# Aidan Liljehorn
# CS 330
# Credit/Sources: Ideas from KnockKnockProtocol from Java

def twenty_questions_protocol(self):
    question = 0
    response = 2
    correct = 3
    too_many = 4

    count = ++1
    state = question
    word = input("Enter a word for the game: ")

    guesses = input("Enter a Y/N question or a guess of the word: ")
    answers = input("Enter 'Yes' or 'No' based on the question: ")
    output = ""

    while count != 21:
        if state == question:
            if count == 20:
                state = too_many
            print("You have ", count, " guesses/questions left.")
            output = guesses
            state = question

        elif state == response:
            if output == word:
                state = correct
            else:
                output = answers
                state = question

        elif state == correct:
            print("The word '", word, "' has been guessed correctly!")
            output = "The game is over, the Guesser has won!"

        elif state == too_many:
            print("The user has guessed too many times.")
            output = "The game is over, the Word Master has won!"

        return output