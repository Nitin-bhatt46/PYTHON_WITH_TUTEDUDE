# match and findall function in re
# match ( pattern, string, flags)

import re
pattern = "apple"
if re.match(pattern , "apple"):
    print("True")
else:
    print( "False" )




## findall( pattern, string, flags)
pattern = "apple"
if re.findall(pattern , "apple is a best fruit"):
    print("True")
else:
    print( "False" )