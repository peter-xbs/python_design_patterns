# _*_ coding:utf-8 _*_

import re
# Usages: 确认一些正则表达式的特殊用法

# 1. ?的用法

# 1) ?P<name>

r = re.search('(?P<name>\w+)\sworld', 'hello world')
print(r.group('name'))
# out: hello

# 2) ?P=name # todo
# r = re.search('(?P<name>\w+)\s\w+(?=name),\w', 'hello world and hello, mike!')
# print(r.group('name'))

# 3) ?= & ?!  lookahead assertion

r1 = re.search('.+(?=l)', 'hello world')
print('3:', r1.group())
# out: hello worl

r2 = re.search('hello(?!\d)', 'hello1 world')
print('4:', r2)
# out: NoneType has no attribute 'group

# 4) ?<= & ?<! lookbehind assertion
r1 = re.search('(?<=hell)\w+', 'hello world')
print('5:', r1)
# out: o
r2 = re.search('(?<!\s)world', 'hello world')
print('6:', r2)
# out: None
r3 = re.search('(?<!o)world', 'hello world')
print('7:', r3)
# out: world

# 5) {m,n}?
"""
Causes the resulting RE to match from m to n repetitions of the preceding RE, 
attempting to match as few repetitions as possible.
"""

# 6) ?:
"""
A non-capturing version of regular parentheses. 
Matches whatever regular expression is inside the parentheses, 
but the substring matched by the group cannot be retrieved after 
performing a match or referenced later in the pattern.
"""
"""
Usages of re.split:
Split string by the occurrences of pattern. 
If capturing parentheses are used in pattern, 
then the text of all groups in the pattern are also returned as part of the resulting list. 
If maxsplit is nonzero, at most maxsplit splits occur, 
and the remainder of the string is returned as the final element of the list.
"""
r1 = re.split('(\d\.)(?!")', '1. you should spend 2." dollars. 2. how are you')
print('8:', r1)
# out: ['', '1.', ' you should spend 2." dollars. ', '2.', ' how are you']
r2 = re.split('(?:\d\.)(?!")', '1. you should spend 2." dollars. 2. how are you')
print('9:', r2)
# out: ['', ' you should spend 2." dollars. ', ' how are you']
r3 = re.findall('(?:\d\.)(?!")', '1. you should spend 2." dollars. 2. how are you')
print('10:', r3)
# Conclusion: capture of non-capture only works on re.split/nest structures, but not works on other regex rules.

# 7) ((?:[a-z]+(?:[-'][a-z]+)*))
text = """
Usages of re.split:
Split string by the occurrences of pattern. 
If capturing parentheses are used in pattern, 
then the text of all groups in the pattern are also returned as part of the resulting list. 
If maxsplit is nonzero, at most maxsplit splits occur, 
and the remainder of the string is returned as the final element of the list.
"""
r1 = re.findall("((?:[a-z]+(?:[-'][a-z]+)*))", text, re.IGNORECASE)
print(r1)
# english tokenizer, very laudably！