# Twenty Questions Protocol
# Aidan Liljehorn
# CS 330
# Credit/Sources: Ideas from KnockKnockProtocol from Java

import socket


class TQP:

    room = []
    username = []
    password = []
    gameword = 'Giraffe'

    def __init__(self):
        self.loggedIn = False
        self.joinedRoom = False
        self.gameFinished= False

    def processInput(self, theInput):
        if not self.loggedIn:
            if theInput.startswith('REG'):
                splitIn = theInput.split()
                TQP.username = splitIn[1]
                TQP.password = splitIn[2]
                theOutput = '[SERVER]You are now registered.'
                self.loggedIn = True

            elif theInput == 'HELP':
                theOutput = 'Hello and welcome to the Twenty Questions Game Lobby!\n' \
                            'Please register in order to login.\nCOMMANDS:\n' \
                            'REG [username , password]\nLIST\nCREATE [name]\n'

            else:
                theOutput = '[SERVER]Please register before using that command.'

        elif not self.joinedRoom:
            if theInput.startswith('REG'):
                theOutput = '[SERVER]You are already registered. Try the HELP command.'

            elif theInput == 'HELP':
                theOutput = 'Hello and welcome to the Twenty Questions Game Lobby!\n' \
                            'COMMANDS:\nREG [username , password]\nLIST\nCREATE [name]\n'

            elif theInput.startswith('CREATE'):
                splitIn = theInput.split()
                TQP.room = splitIn[1]
                theOutput = '[SERVER]Room created.'

            elif theInput.startswith('JOIN'):
                theOutput = '[SERVER]You have joined a room'
                self.joinedRoom = True

        elif not self.gameFinished:
            game_start = 0
            game_count = 0
            if game_start == 0:
                theOutput = '[SERVER]Please ask YES or NO questions and or guess what the word is! (No ?s after question)'
                game_start += 1
            elif game_count > 20:
                theOutput = '[SERVER]You have asked too many questions, you lose.'
                self.joinedRoom = False
            elif theInput.lower() == 'Is it an animal' or 'Is it yellow' or 'Is it tall' or 'Is it big'\
                    or 'Is it in a zoo' or 'Does it only eat plants':
                game_count += 1
                theOutput = 'Yes'
            elif theInput.lower() == 'Giraffe':
                theOutput = '[SERVER]You have guessed the word correctly, you win!'
                self.joinedRoom = False
            else:
                game_count += 1
                theOutput = 'No'

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
