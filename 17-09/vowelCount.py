'''
    Function Argument --> Sentence 
    parse the sentence to calculate vowels
'''

def CountVowel(word):
    print("Given String {0}".format(word))
    word = word.lower()

    return {
        var:word.count(var) for var in 'aeiou'
    }


if __name__ == '__main__':
    result = CountVowel("I love Python Programming")
    print(result)