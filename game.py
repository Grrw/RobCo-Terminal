import json, random, curses

def game(stdscr, difficulty):

    level = difficulty

    def wordGetter():
        """ Gets words from a list, returning them
        easy (5 letters, 3 words), 
        medium (7 letters, 5 words),
        hard (9 letters, 7 words) """
        nonlocal level
        with open('words.json') as words_:
            word_data = json.load(words_)
        
        wrdSet = random.randint(0,3)

        if level == "easy":
            return(word_data["Easy"][wrdSet])
        elif level == "medium":
            return(word_data["Medium"][wrdSet])
        elif level == "hard":
            return(word_data["Hard"][wrdSet])

    # def initrand(user_list, diff):
    #     """ Takes words from the list,
    #     returning 5 random words """
    #     retList = []
    #     if diff == 'easy':
    #         wrdAmt = 3
    #     elif diff == 'medium':
    #         wrdAmt = 5
    #     elif dff == 'hard':
    #         wrdAmt = 7

    #     for x in range(wrdAmt):
    #         popper = random.randrange(0, len(user_list))
    #         retList.append(user_list[popper])
    #         user_list.pop(popper)
    #     return retList

    """ GAMES START HERE """
    diffList = wordGetter()
    
    ### temporary starts
    stdscr.addstr(13,10,'                                              ')
    stdscr.addstr(13,10,str(diffList),curses.color_pair(1))
    ### temporary ends


    if level == 'easy':
        pass
    elif level == 'medium':
        pass
    elif level == 'hard':
        pass
