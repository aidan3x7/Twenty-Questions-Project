# Twenty Questions Protocol
# Aidan Liljehorn
# CS 330
# Credit/Sources: Ideas from KnockKnockProtocol from Java

import socket


class TQP:

    open_room = []
    joined_room = []
    username = []
    gamecount = 0
    gameword = 'Giraffe'
    room_count = 0

    def __init__(self, user, user_room):
        self.loggedIn = False
        self.joinedRoom = False
        self.gameStart = False
        self.gameFinished = False
        self.user = user
        self.user_room = user_room

    def processInput(self, theInput):
        if not self.loggedIn:
            if theInput.lower().startswith('reg'):
                splitIn = theInput.split()
                self.user = splitIn
                TQP.username.append(splitIn[1])
                theOutput = '[SERVER]You are now registered'
                self.loggedIn = True

            elif theInput.lower() == 'help':
                theOutput = 'Hello and welcome to the Twenty Questions Game Lobby!\n' \
                            'Please register in order to login.\nCOMMANDS:\n' \
                            'REG [username]\nLIST\nUSERS\nCREATE [name]\nHELP'

            else:
                theOutput = '[SERVER]Please register before using that command.'

        elif not self.joinedRoom:
            if theInput.lower().startswith('reg'):
                theOutput = '[SERVER]You are already registered. Try the HELP command.'

            elif theInput.lower() == 'help':
                theOutput = 'Hello and welcome to the Twenty Questions Game Lobby!\n' \
                            'COMMANDS:\nLIST\nCREATE [name]\nJOIN [name]'

            elif theInput.lower() == 'list':
                list_convert = ''
                count = 0
                for i in TQP.open_room:
                    list_convert += '\n' + str(count) + ':' + i
                    count += 1
                theOutput = list_convert

            elif theInput.lower() == 'users':
                list_convert = ''
                count = 0
                for i in TQP.username:
                    list_convert += '\n' + str(count) + ':' + i
                    count += 1
                theOutput = list_convert

            elif theInput.lower().startswith('create'):
                TQP.room_count += 1
                splitIn = theInput.split()
                TQP.open_room.append(splitIn[1])
                theOutput = '[SERVER]Room created.'

            elif theInput.lower().startswith('join'):
                splitIn = theInput.split()
                room_select = TQP.open_room.index(splitIn[1])
                TQP.joined_room.append(TQP.open_room[room_select])
                if TQP.joined_room.count(splitIn) == 2:
                    TQP.open_room.remove(splitIn)
                    user_replace = TQP.joined_room.index(splitIn)
                    TQP.joined_room.insert(user_replace, self.user)
                self.user_room = splitIn
                theOutput = '[SERVER]You have joined a room'
                self.joinedRoom = True

            else:
                theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'

        elif not self.gameStart:
            theOutput = '[SERVER]Please ask YES or NO questions and or guess what the word is! (No ?s after question)'
            self.gameStart = True

        elif not self.gameFinished:
            TQP.gamecount += 1
            if TQP.gamecount > 20:
                theOutput = '[SERVER]You have asked too many questions, you lose.'
                self.joinedRoom = False

            elif theInput.lower() == 'giraffe':
                theOutput = '[SERVER]You have guessed the word correctly, you win!'
                self.joinedRoom = False

            else:
                print(theInput)
                theOutput = input("Please enter ~Yes~ or ~No~ based on the clients question:\n")

            print(TQP.gamecount)

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
