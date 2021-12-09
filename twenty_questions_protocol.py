# Twenty Questions Protocol
# Aidan Liljehorn
# CS 330
"""
Credit/Sources: Some ideas from KnockKnock Java code
https://stackoverflow.com/questions/31925964/python-check-if-string-split-succeeded
"""

import socket


class TQP:

    open_room = []
    joined_room = []
    username = []
    room_count = 0

    def __init__(self, user, user_room, user_room_index, word):
        self.loggedIn = False
        self.joinedRoom = False
        self.gameStart = False
        self.gameFinished = False
        self.one_user = False
        self.guesser = False
        self.user = user
        self.user_room = user_room
        self.user_room_index = user_room_index
        self.word = word
        self.game_count = 0

    def processInput(self, theInput):
        if not self.loggedIn:
            if theInput.lower().startswith('reg'):
                splitIn = theInput.split(' ', 1)
                if len(splitIn) < 2:
                    theOutput = 'Hello and welcome to the Twenty Questions Game Registration!\n' \
                                'Please register in order to login.\n' \
                                'COMMANDS:\n' \
                                'REG [username]'
                else:
                    noncommand = splitIn[1]
                    if TQP.username.count(noncommand) == 1:
                        theOutput = '[SERVER]Username already in use, please try again.'

                    else:
                        self.user = noncommand
                        TQP.username.append(noncommand)
                        theOutput = '[SERVER]You are now registered: ' + noncommand
                        self.loggedIn = True

            elif theInput.lower() == 'help':
                theOutput = 'Hello and welcome to the Twenty Questions Game Registration!\n' \
                            'Please register in order to login.\n' \
                            'COMMANDS:\n' \
                            'REG [username]'

            else:
                theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'

        elif not self.joinedRoom:
            if theInput.lower().startswith('reg'):
                theOutput = '[SERVER]You are already registered. Try the HELP command.'

            elif theInput.lower() == 'help':
                theOutput = 'Hello and welcome to the Twenty Questions Game Lobby!\n' \
                            'COMMANDS:\n' \
                            'LIST          -- Shows a list of the Open Rooms\n' \
                            'USERS         -- Shows a list of all Users\n' \
                            'CREATE [name] -- Creates a room with a specified name\n' \
                            'JOIN [name]   -- Joins a room with a specified name'

            elif theInput.lower() == 'list':
                if len(TQP.open_room) == 0:
                    theOutput = '[SERVER]There are currently no rooms.'

                else:
                    list_convert = ''
                    count = 0
                    for i in TQP.open_room:
                        list_convert += str(count) + ': ' + i + '\n'
                        count += 1
                    theOutput = list_convert

            elif theInput.lower() == 'users':
                list_convert = ''
                count = 0
                for i in TQP.username:
                    list_convert += str(count) + ': ' + i + '\n'
                    count += 1
                theOutput = list_convert

            elif theInput.lower().startswith('create'):
                splitIn = theInput.split(' ', 1)
                if len(splitIn) < 2:
                    theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'

                else:
                    noncommand = splitIn[1]
                    if TQP.open_room.count(noncommand) == 1:
                        theOutput = '[SERVER]A room with name already exists.'

                    else:
                        TQP.room_count += 1
                        TQP.open_room.append(noncommand)
                        theOutput = '[SERVER]Room created: ' + noncommand

            elif theInput.lower().startswith('join'):
                splitIn = theInput.split(' ', 1)
                if len(splitIn) < 2:
                    theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'

                else:
                    noncommand = splitIn[1]
                    if TQP.open_room.count(noncommand) == 0:
                        theOutput = '[SERVER]That room does not exist.'

                    else:
                        TQP.joined_room.append(noncommand)
                        if TQP.joined_room.count(noncommand) == 2:
                            TQP.open_room.remove(noncommand)
                        self.user_room = noncommand
                        theOutput = '[SERVER]You have joined a room'
                        self.user_room_index = TQP.joined_room.index(noncommand)
                        self.joinedRoom = True

            else:
                theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'

        elif not self.gameStart:
            if TQP.joined_room.count(self.user_room) == 1:
                if TQP.joined_room[self.user_room_index] != self.user_room:
                    self.word = TQP.joined_room[self.user_room_index]
                    TQP.joined_room[self.user_room_index] = '--'
                    theOutput = '[SERVER]You are the Guesser, please ask yes or no questions!'
                    self.guesser = True
                    self.gameStart = True
                else:
                    theOutput = '[SERVER]Cannot start until another user joins'

            elif TQP.joined_room.count(self.user_room) == 2:
                if theInput.lower().startswith('start'):
                    splitIn = theInput.split(' ', 1)
                    if len(splitIn) < 2:
                        theOutput = 'Please use the command START [word] to start the game either as the WordMaster' \
                                    'or the Guesser.'
                    else:
                        noncommand = splitIn[1]
                        TQP.joined_room[self.user_room_index] = noncommand
                        self.word = noncommand
                        theOutput = '[SERVER]You are the WordMaster, please answer Yes or No ONLY to questions!'
                        self.wordmaster = True
                        self.gameStart = True

                else:
                    theOutput = 'Please use the command START [word] to start the game either as the WordMaster' \
                                'or the Guesser.'

        elif not self.gameFinished:

            if self.game_count > 20:
                if self.guesser:
                    theOutput = '[SERVER]You have asked too many questions, you lose.'
                    TQP.joined_room[self.user_room_index] = 'THE GUESSER HAS LOST HOPEFULLY THIS IS NOT TYPED IN'
                    self.joinedRoom = False
                    self.gameStart = False
                    self.gameFinished = False

            elif TQP.joined_room[self.user_room_index] == 'THE GUESSER HAS LOST HOPEFULLY THIS IS NOT TYPED IN':
                theOutput = '[SERVER]The guesser has asked too many questions, you win.'
                self.joinedRoom = False
                self.gameStart = False
                self.gameFinished = False

            elif theInput.lower().startswith('guess'):
                splitIn = theInput.split(' ', 1)
                if len(splitIn) < 2:
                    theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'
                else:
                    noncommand = splitIn[1]
                    if noncommand == self.word:
                        if self.guesser:
                            theOutput = '[SERVER]You have guessed the word correctly, you win!'
                            TQP.joined_room[self.user_room_index] = self.word
                            self.joinedRoom = False
                            self.gameStart = False
                            self.gameFinished = False
                        else:
                            theOutput = '[SERVER]Yes...that is the word you chose.'

            elif TQP.joined_room[self.user_room_index] == self.word:
                theOutput = '[SERVER]The guesser has guessed correctly, you lose.'
                self.joinedRoom = False
                self.gameStart = False
                self.gameFinished = False

            elif theInput.lower() == 'check':
                theOutput = TQP.joined_room[self.user_room_index]

            elif theInput.lower().startswith('enter'):
                self.game_count += 1
                splitIn = theInput.split(' ', 1)
                if len(splitIn) < 2:
                    theOutput = '[SERVER]Unknown command, please use HELP for list of commands.'
                else:
                    noncommand = splitIn[1]
                    if not self.guesser:
                        if noncommand.lower() != 'yes' or 'no':
                            theOutput = '[SERVER]You can only ENTER [YES] or [NO]'

                    else:
                        theOutput = '[SERVER]Please use the CHECK command to see if the other' \
                                    ' client has responded before using enter again.'
                        TQP.joined_room[self.user_room_index] = noncommand

            elif theInput.lower() == 'help':
                if self.guesser:
                    theOutput = '[SERVER]Commands:\n' \
                                'ENTER [...] -- To ask a Yes or No question\n' \
                                'CHECK -- Check to see if WordMaster has answered your question\n' \
                                '(You guess by just typing in your guess without a no command)'
                else:
                    theOutput = '[SERVER]Commands:\n' \
                                'ENTER [...] -- To answer the question with either YES or NO (ONLY)\n' \
                                'CHECK --  Check to see if guesser has asked another question'

            else:
                if self.guesser:
                    theOutput = '[SERVER]Commands:\n' \
                                'ENTER [...] -- To ask a Yes or No question\n' \
                                'CHECK -- Check to see if WordMaster has answered your question\n' \
                                '(You guess by just typing in your guess without a no command)'

                else:
                    theOutput = '[SERVER]Commands:\n' \
                                'ENTER [...] -- To answer the question with either YES or NO (ONLY)\n' \
                                'CHECK --  Check to see if guesser has asked another question'

        return theOutput

