def create_words(words, cards):
    """
    A function that receives a dictionary with words and values, and cards containing letters. The function returns the word with the highest value from the dictionary that can be assembled using the letter cards
    :param words: A dictionary containing keys that are words and values that are a score for each word
    :param cards: A list of letters we can use to make the words
    :return: The function returns the word with the highest value that can be assembled from the existing letter cards
    """
    def count_cards_letters(cards, cards_dict): #A function that creates a dictionary whose keys are the letters of the cards and the values are the count of how many times each letter appears in the cards
        if cards_dict is None:
            cards_dict = {}
        if not cards:
            return cards_dict #The stopping condition is if we have finished going through all the cards
        current_letter = cards[0]
        cards_dict[current_letter] = cards_dict.get(current_letter, 0) + 1 #If a letter is already in the dictionary, we will add 1 to its value, if not, we will add the letter to the dictionary with the value 1
        return count_cards_letters(cards[1:], cards_dict) #Reducing the problem is done by removing the card we have already inserted into the dictionary

    def count_words_letters(word, counter): #A function that creates a dictionary whose keys are the letters of the word with the highest value and the values are the count of how many times each letter appears in the word
        if counter is None:
            counter = {}
        if not word:
            return counter #The stopping condition is if we have finished going through the word
        current_letter = word[0]
        counter[current_letter] = counter.get(current_letter, 0) + 1 #If a letter is already in the dictionary, we will add 1 to its value, if not, we will add the letter to the dictionary with the value 1
        return count_words_letters(word[1:], counter) #Reducing the problem is done by removing the letter  we have already inserted into the dictionary

    def can_form_highest_word(highest_word, cards_count): #The function compares the dictionary we created for the word with the highest value and the dictionary of the cards
        if not highest_word: #The stopping condition is if we have finished going through the word
            return True
        letter = highest_word[0]
        if cards_count.get(letter, 0) > 0: #If the letter is in the dictionary of the cards, we subtract one from it
            cards_count[letter] -= 1
            return can_form_highest_word(highest_word[1:], cards_count)  #Reducing the problem is done by removing the letter we have already checked
        return False

    def find_highest_value_recursive(words, highest_word, highest_value): #A function for finding the highest value that exists in the words dictionary
        if not words: #The stopping condition is if we have gone through all the keys (words) in the dictionary
            return highest_word
        current_word, current_value = words.popitem() #Each time we will randomly select a word that we will take out of the dictionary and check if its value is greater than the value of the previous word we checked. If so, we will update it to be the word with the highest value
        if current_value > highest_value:
            highest_word, highest_value = current_word, current_value
        return find_highest_value_recursive(words, highest_word, highest_value)

    def final_func(words, cards_count):
        if not words: #If there are no words in the dictionary
            return ''
        highest_word = find_highest_value_recursive(words.copy(),None, 0) #First we call the function that finds the word with the highest value
        if can_form_highest_word(highest_word, cards_count.copy()): #After that we will check if we can use the letters on our cards to form the word with the highest value
            return highest_word #If the word with the highest value can be assembled, we will return it
        del words[highest_word] #If the word with the highest value cannot be assembled, we delete it from the list and look for the next word with the highest value
        return final_func(words, cards_count)

    cards_count = count_cards_letters(cards , None)
    return final_func(words.copy(), cards_count)
