# regular expression

# mostly prefer for the string.
# it validate the input

import re
pattern = "apple"
if re.match(pattern , "apple"):
    print("True")
else:
    print( "False" )