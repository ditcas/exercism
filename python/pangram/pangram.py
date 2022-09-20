import string

def is_pangram(sentence: str) -> bool:
    """
    Determine if a sentence is a pangram, i.e. a sentence using every letter of the alphabet at least once.
    
    :param sentence: str - sentence to analyze
    :return: bool - true if the sentence is a pangram

    """
    
    line = sentence
    # Delete punctuation signs and numbers.
    line = line.translate(line.maketrans("","",string.punctuation))
    line = line.translate(line.maketrans("","",string.digits)) 
    line = line.lower() # All words in lowercase
    words = line.split() # Generate the list of words

    letters = set()

    for word in words:
        letters |= set(word) # Transform the words into letters and keep all of them only once. Union of sets.

    return set(letters) == set(string.ascii_lowercase) # Compare with the set that contains alphabet (a-z).


# def is_impossible_pangram(sentence: str) -> bool:
#     """
#     Determine if a sentence is an impossible pangram, i.e. a sentence using EVERY letter of the alphabet ONLY once.
    
#     :param sentence: str - sentence to analyze
#     :return: bool - true if the sentence is an impossible pangram

#     """
    # count_letters = dict()

    # for word in words:
    #     word_letters = list(word)
    #     for letter in word_letters:
    #         count_letters[letter] = count_letters.get(letter, 0) + 1

    # if set(count_letters.keys()) != set(string.ascii_lowercase):
    #     return False
    
    # if sum(list(count_letters.values())) != 26: # An easy comparative that helps us to discard a false case, unless it's not definitve.
    #     return False
    
    # for value in count_letters.values():
    #     if value != 1:
    #         return False

    # return True