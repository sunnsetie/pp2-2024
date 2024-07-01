import re
text = "HelloWorld"
print(re.findall('[A-Z][^A-Z]*', text))