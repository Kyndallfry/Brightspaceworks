# Brightspaceworks
def countthevowels(v: str):
    v = set(v.lower())
    return sum([vowel in v for vowel in 'aeiou'])
countthevowels("data")

