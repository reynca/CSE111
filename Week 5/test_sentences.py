import pytest
from sentences import *

def test_get_determiner():
    determ = get_determiner(1)
    words = ["a", "one", "the"]
    assert determ in words
    determ = get_determiner(2)
    words = ["two", "some", "many", "the"]
    assert determ in words

def test_get_noun():
    noun = get_noun(1)
    words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    assert noun in words
    noun = get_noun(2)
    words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    assert noun in words

def test_get_verb():
    assert get_verb(1 or 2, "past") == "drank" or "ate" or "grew" or "laughed" or "thought" or "ran" or "slept" or "talked" or "walked" or "wrote"
    assert get_verb(1, "present") == "drinks" or "eats" or "grows" or "laughs" or "thinks"\
         or "runs" or "sleeps" or "talks" or "walks" or "writes"
    assert get_verb(2, "present") == "drink" or "eat" or "grow" or "laugh" or "think" or "run" or "sleep" or "talk" or "walk" or "write"
    assert get_verb(1 or 2, "future") == "will drink" or "will eat" or "will grow" or "will laugh"\
         or "will think" or "will run" or "will sleep" or "will talk" or "will walk" or "will write"

def test_get_preposition():
    assert get_preposition() == "about" or "above" or "across" or "along" or"around" or "at" or "after" or "before" or "behind" or "below" or"beyond" or "by" or "despite" or "except" or "for" or"from" or "in" or "into" or "near" or "of" or "off" or "on" or "onto" or "out" or "over" or "past" or "to" or "under" or "with" or "without"
    

def test_get_prepositional_phrase():
    pass

pytest.main(["-v", "--tb=line", "-rN", __file__])