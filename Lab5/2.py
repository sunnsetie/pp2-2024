import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Match'
        else:
                return('Not matched')
print(text_match("ab"))
print(text_match("aabbbbbc"))