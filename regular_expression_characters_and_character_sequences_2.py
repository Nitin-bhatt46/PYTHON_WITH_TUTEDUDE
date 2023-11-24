# character and character sequence.

# * - repeat a character zero or more times
# + - repeat a character one or more times
# ( - Indicates where string extraction is to start
# ) - indicates where string extraction is to end
# ? - Matches the expression 0 to 1 times.


import re
string = "It is a dog"
pattern = "i*"
print(re.findall(pattern, string))

import re
string = "It is a dog"
pattern = "i+"
print(re.findall(pattern, string))

import re
string = "It is a dog"
pattern = "^It (\D)"
print(re.findall(pattern, string))


import re
string = "It is a dog"
pattern = "^I.*?"
print(re.findall(pattern, string))