#search and replace

import re

phone = "2004- 959-559 #This is a phone number"

#Delete marks that are not numbers (#)
num = re.sub (r'#.*$', "", phone)
print "Phone Num :", num

#remove anything other than digits
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num

