def CountVowel(word):
    print ("Given String {0}".format(word))
    word = word.lower()
    return {
            v:word.count(v) for v in 'aeiou'
            }


if __name__ == '__main__':
    res = CountVowel("I Love Python Programming")
    print(res)
