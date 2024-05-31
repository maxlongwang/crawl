import re

print(re.match(r'l', 'liuyan1').group())  # 返回l
print(re.match(r'y', 'liuyan1'))  # 返回None
print(re.search(r'y', 'liuyan1').group())  # 返回y

text = "Hello, my name is John Doe."
match = re.search(r"Hello, my name is (\w+) (\w+)", text).group()
print(match)

match = re.search(r"Hello, my name is (\w+) (\w+)", text).groups()
print(match)

text = "Hello, my name is John Doe."
match = re.search(r"Hello, my name is (?P<first_name>\w+) (?P<last_name>\w+)", text).groupdict()

print(match)
