import pytest

'''
You decide to create a substitution cipher. The cipher alphabet is based on a key shared amongst those of your friends who don't mind spoilers.

Suppose the key is:
"The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!".

We use only the unique letters in this key to set the order of the characters in the substitution table.

T H E Q U I C K O N Y X G B L R A S W D J M P V Z F

(spaces added for readability)

We then align it with the regular alphabet:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T H E Q U I C K O N Y X G B L R A S W D J M P V Z F
Which gives us the substitution mapping: A becomes T, B becomes H, C becomes E, etc.

Write a function that takes a key and a string and encrypts the string with the key.

Example:
key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"
encrypt("It was all a dream.", key) -> "Od ptw txx t qsutg."
encrypt("Would you kindly?", key) -> "Pljxq zlj yobqxz?"

Complexity analysis:

m: The length of the message
k: The length of the key

{
    "T": True,
    "H": True
    ...
}
lst = []

'''


class Solution():
    def substitution_cipher(self, message, key):
        # build the cipher
        dct = {}
        lst = []
        _A, _Z, _a, _z = ord('A'), ord('Z'), ord('a'), ord('z')
        for c in key:
            char = c.upper()
            if not dct.get(char, False):
                if _A <= ord(c) <= _z:
                    dct[char] = True
                    lst.append(char)
        dct_2 = {}
        for i, v in enumerate(
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']):
            dct_2[v] = lst[i].upper()
        # convert the message
        result = []
        for c in message:
            char = c.upper()
            if _A <= ord(c) <= _Z:
                result.append(dct_2.get(char, ''))
            elif _a <= ord(c) <= _z:
                result.append(dct_2.get(char, '').lower())
            else:
                result.append(c)
        return ''.join(result)


key = "The quick onyx goblin, Grabbing his sword ==}-------- jumps over the 1st lazy dwarf!"


@pytest.mark.parametrize("message,key,expected", [
    ('It was all a dream.', key, 'Od ptw txx t qsutg.'),
    ('Would you kindly?', key, 'Pljxq zlj yobqxz?')
])
def test_answer(message, key, expected):
    assert Solution().substitution_cipher(message, key) == expected
