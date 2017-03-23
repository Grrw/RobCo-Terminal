import json, random

def game(difficulty):

    level = difficulty

    def wordGetter():
        """
        Gets words from a list, returning them
        levels are: easy (5 letters), medium (7 letters), hard (9 letters)
        """
        nonlocal level
        with open('words.json') as words_:
            word_data = json.load(words_)
        if level == "easy":
            return(word_data["Easy"])
        elif level == "medium":
            return(word_data["Medium"])
        elif level == "hard":
            return(word_data["Hard"])

    def initrand(user_list):
        """
        Takes words from the list, returning 5 random words
        """
        startupList = []
        for x in range(5):
            popper = random.randrange(0, len(user_list))
            startupList.append(user_list[popper])
            user_list.pop(popper)
        return startupList

    diffList = wordGetter()
    diffList = initrand(diffList)
    
    if level == 'easy':
        pass
    elif level == 'medium':
        pass
    elif level == 'hard':
        pass
