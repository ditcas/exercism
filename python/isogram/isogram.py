import string

def is_isogram(phrase):
    """
    Determine if a word or phrase is an isogram, i.e. each letter appears only once.
    Spaces and hyphens are allowed to appear multiple times.

    :param phrase: str - word or phrase to analyze

    :return: bool - True if the given string is an isogram.
    """

    letters = [letter for letter in phrase.lower() if "a" <= letter <= "z"] # Si és una lletra, posa-la en minúscula i guarda-la.

    return len(letters) == len(set(letters))


"""-------------------------Codi segona iteració---------------------------------------"""

    # def remove_punctuation(phrase):
    #     phrasewp = phrase.translate(phrase.maketrans("","",string.punctuation))
    #     return phrasewp
    # def remove_digits(phrase):
    #     phrasewd = phrase.translate(phrase.maketrans("","",string.digits)) 
    #     return phrasewd
    # def remove_spaces(phrase):
    #     phrasews = phrase.replace(" ", "")
    #     return phrasews
    # # Delete punctuation signs and numbers. All words in lowercase. All words together without whitespaces.
    # clean_func = [remove_punctuation, remove_digits, str.lower, remove_spaces]
    # for function in clean_func:
    #     phrase = function(phrase)

    # for pos in range(0, len(phrase)-1): # posicions de cada lletra sense incloure l'última
    #     if phrase[pos] in phrase[pos+1:]: # si la lletra està repetida en el que queda de string
    #         return False

    # return True

"""-----------------------------Codi primera iteració-------------------------------------"""

# letters = list(phrase) # Transform words into separated letters

    # count_letters = {} # Count how many times appears each letter

    # for letter in letters:
    #     count_letters[letter] = count_letters.get(letter, 0) + 1
    
    # for value in count_letters.values(): # If some value count is not 1 then is just not an isogram
    #     if value != 1:
    #         return False