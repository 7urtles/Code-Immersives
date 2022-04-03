from random import randint
from string import ascii_lowercase

class wordOps:
    def __init__(self, word):
        self.word = word
        self.vowels = tuple('aeiou')
        self.consonants = tuple(self.remove_vowels(ascii_lowercase))

    def remove_vowels(self, input_string = False, replacer='_'):
        word = input_string if input_string else self.word
        for vowel in self.vowels:
            word = word.replace(vowel,f"{replacer}")
        return word

    def strip_consonants(self, replacer='_'):
        word = self.word
        for consonant in self.consonants:
            word = word.replace(consonant,f"{replacer}")
        return word

    def strip_fixed(self, step_count,replacer='_'):
        word = self.word

        for num in range(0, len(word), step_count):
            word = word[:num] + f"{replacer}" + word[num+1:]
        return word

    def show(self):
        word = self.word
        consonants,vowels = 0,0
        for letter in word:
            if letter in self.consonants:
                consonants+=1
            elif letter in self.vowels:
                vowels+=1
        return f"\nWord: {self.word}\nConsonants: {consonants}\nVowels: {vowels}\n"

    def rand_remove(self, amount_to_remove, replacer='_'):
        word = self.word
        # check if user requested to remove more characters are in string
        if len(word) < amount_to_remove: raise IndexError('Index too high')

        # iterate amount of times specified
        for _ in range(amount_to_remove):
            # pick a random index of the word
            position = randint(0, len(word))
            # remove the letter at that index
            word = word[:position-1] + f"{replacer}" + word[position:]
        return word


# for any replacer function, give an extra argument as a char to change the replacement character "_" by default
word = wordOps('hello world')
print(f'No vowels: {word.remove_vowels()}\n')
print(f'No consonants: {word.strip_consonants()}\n')
print(f"Removing by step: {word.strip_fixed(2, '-')}\n")
print(f'Info: {word.show()}')
print(f'Removing random indices: {word.rand_remove(3)}')