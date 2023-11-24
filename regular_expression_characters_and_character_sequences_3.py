# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character.
# [a-z 0-9 ] - set of characters can include a range.
# {}

import re
string = "It is a dog"
pattern = "[aeiou]"
print(re.findall(pattern, string))


import re
string = "It is a dog"
pattern = "[^xyz]"
print(re.findall(pattern, string))

import re
string = "It is a dog"
pattern = "[a-z 0-9]"
print(re.findall(pattern, string))


import re
string = "Itt is a dog"
pattern = "It{1}"
print(re.findall(pattern, string,flags=0))