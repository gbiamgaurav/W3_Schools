#import re

#txt = "The Rain in Spain"
#x = re.search("^The.*Spain$", txt)

#print(x)

import re

txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)

x = re.findall('portugal', txt)
print(x)

txt = "The Rain in Spain"
x = re.search("\s", txt)

print("The first white spaced character located in position: ", x.start())


