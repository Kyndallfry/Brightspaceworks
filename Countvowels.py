# Brightspaceworks
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])


def count_vowels(args):
    vowels = set()

    for arg in args:
        for char in arg:
            if char.lower() in 'aeiou':
                vowels.add(char)
    return len(vowels)

print(count_vowels(sys.argv[1:]))
