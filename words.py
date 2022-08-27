def print_upper_words(words):
    """For a given list of words, print out each word on a separate line, but in all uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(["banana", "apple", "orange", "apricot"])
print("")

def print_upper_words_starts_with_e(words):
    """For a given list of words, prints all words in uppercase that start with the letter ‘e’ (either upper or lowercase)"""
    for word in words:
        if word.lower().startswith("e"):
            print(word.upper())

print_upper_words_starts_with_e(["Eagle", "wolF", "Lion", "tiger", "elk", "EMU"])
print("")
    

def print_upper_words(words, must_start_with):
    """Given list of words and set of letters, return list of UPPERCASED words each starts with one of those letters.

    For example:
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

    this should print "HELLO", "HEY", "YO", and "YES"
    """ 
    new_words = []
    for word in words:
        for key in must_start_with:
            if word.lower().startswith(key.lower()):
                new_words.append(word.upper())
    print(new_words)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
print_upper_words(["Hello", "hey", "Goodbye", "yo", "yes"], must_start_with={"h", "G"})
