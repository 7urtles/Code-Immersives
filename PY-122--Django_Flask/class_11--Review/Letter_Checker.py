word = 'disassemble'
lst1 = ['a','i','z','v','s','e','a','d','s','e','r','m','m','e','s','l']
lst2 = ['a','t','r','l','s','e','a','d','s','5','r','g','w','e']
lst3 = ['f','f','r','a','r']

def solution1(word, list1):
    # split word into list
    word = [letter for letter in word]
    # split letters into list of unique letters
    letters = set(word)
    # will hold key value pairs of letters and how many times they occur
    counts1 = {}
    counts2 = {}
    # iterate unique letters and get counts in the word and random letter list
    for i in letters:
        counts1[i] = word.count(i)
        counts2[i] = list1.count(i)
    # iterate letters in word
    for i in counts1:
        # the try is preventing dictionary access if a letter does not exist in both lists
        try:
            # ensure there are less letters in the word than in random letters list
            if counts1[i] <= counts2[i]:
                # if so keep looping
                pass
            else:
                # otherwise there are not enough letters, return false
                return False
        except:
            # if dict access error occurs, a letter does not exist in the random letter list
            return False
    # if the program completes, there are enough letters to make the word
    return True
print(solution1('disassemble',lst1))


def solution2(word,list1):
    # iterate unique letters
    for i in set(word):
        #compare counts of both, if starting word has more of a letter than the list, FALSE
        if word.count(i) > list1.count(i):
            return False
    return True
print(solution2('disassemle',lst1))