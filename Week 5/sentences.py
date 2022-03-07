import random

def main():
    # x = 0
    # tense_type = ["past", "present", "future"]

    
    get_prepositional_phrase(1, "past")
    get_prepositional_phrase(1, "present")
    get_prepositional_phrase(1, "future")
    get_prepositional_phrase(2, "past")
    get_prepositional_phrase(2, "present")
    get_prepositional_phrase(2, "future")

    # tense = random.choice(tense_type)
    # quantity = random.randint(1,2)
    # while x != 6:
    #     # print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity, tense)}.")
    #     get_prepositional_phrase(quantity, tense)
    #     x += 1


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    # word = word.capitalize()
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    else:
        print("ERROR")
    word = random.choice(words)
    return word

def get_preposition():
    words = ["about", "above", "across", "along","around", "at", "after", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity, tense):
    phrase = print(f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)} {get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}")
    return phrase


main()