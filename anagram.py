def isAnagram(word1, word2):
    print(f"Checking {word1} vs {word2} ")
    if len(word1) != len(word2):
        print ("Nope - diff lengths")
        return False;

    for char in word1:
        if char not in word2:
            print (f"Nope - word1 has {char} which is not in {word2} ")
            return False;

    print(f"Yup - {word1} and {word2} are anagrams")
    return True;



assert isAnagram("note", "tone")
assert not isAnagram("note", "dummmmmmm")
assert not isAnagram("noter", "tonem")
