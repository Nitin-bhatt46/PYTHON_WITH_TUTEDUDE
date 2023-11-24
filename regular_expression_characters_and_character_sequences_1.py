# characters and character sequences

# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digits
# \D - Matches any non digit
# \s - Matches whiltespace
# \S - Matches any non-whitespace


import re
string = "It is a dog"
pattern = "^I"
print(re.findall(pattern, string, flags=0))

import re
string = "It is a dog"
pattern = "g$"
print(re.findall(pattern, string, flags=0))

import re
string = "It is a dog"
pattern = "d.."
print(re.findall(pattern, string, flags=0))


import re
string = "It is a dog 6"
pattern = "\d"
print(re.findall(pattern, string, flags=0))


import re
string = "It is a dog 6"
pattern = "\D"
print(re.findall(pattern, string, flags=0))

import re
string = "It is a dog 6"
pattern = "\s"
print(re.findall(pattern, string, flags=0))


import re
string = "It is a dog 6"
pattern = "\S"
print(re.findall(pattern, string, flags=0))