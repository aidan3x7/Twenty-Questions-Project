# Twenty Questions Protocol
# Aidan Liljehorn
# CS 330
# Credit/Sources: Ideas from KnockKnockProtocol from Java

import socket

class TQP:

        CONNECTION = 0
        REGISTER = 1
        state = REGISTER

        username = []
        password = []
        cnum = 0

        def processInput(theInput):
            theOutput = ''
            if TQP.state == TQP.CONNECTION:
                theOutput = 'Connection Established.'
                input('\n')
                if theInput == 'REG':
                    TQP.state == TQP.REGISTER
                else:
                    input('Invalid command.')

            elif TQP.state == TQP.REGISTER:
                regCheck = theInput.split()
                if regCheck[0] == 'REG':
                    inputPop = theInput.replace('REG', '')
                    splitInput = inputPop.split()
                    TQP.username[TQP.cnum] = splitInput[0]
                    TQP.password[TQP.cnum] = splitInput[1]
                else:
                    print('Error: Try again.')

            return theOutput


'''
        client.send("[REGISTER]: Please register for an account.")
        username = client.send(input("[REGISTER]: Please create a username: "))
        username

        password = client.send(input("[REGISTER]: Please create a password: "))
        password


    def login(client, username, password):
        client.send("Please confirm your username and password to login.")
        login_username = client.send(input("[LOGIN]: Enter username: "))
        login_password = client.send(input("[LOGIN]: Enter password: "))

        if login_username != username:
            client.send("[LOGIN]: INCORRECT USERNAME!")
            client.send(login(username, password))

        elif login_password != password:
            client.send("[LOGIN]: INCORRECT PASSWORD!")
            client.send(login(username, password))

        else:
            client.send("[LOGIN]: Successfully logged in, Welcome", username + "!")


    def twenty_qs():
        question = 0
        response = 1
        correct = 2
        state = question

        count = 0

        word = input("[WORDMASTER]Enter a word for the game: ")
        guesses = ""
        answers = ""

        while count != 21:

            if state == question:
                count = count + 1
                if count == 20:
                    print("[SERVER]The user has guessed too many times.")
                    return "[SERVER]The game is over, the Word Master has won!"
                guesses = input("[GUESSER]Enter a Y/N question or a guess of the word: ")
                state = response
                print(count)

            elif state == response:
                if guesses == word:
                    state = correct
                    print(count)

                elif guesses != answers:
                    answers = input("[WORDMASTER]Enter 'Yes' or 'No' based on the question: ")
                    state = question
                    print(count)

            elif state == correct:
                print("[SERVER]The word '", word, "' has been guessed correctly!")
                print(count)
                return "The game is over, the Guesser has won!"
'''
