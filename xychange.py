git statusPython 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # заменить все буквы "х" на "у"

orginal_string = "xyyx yyxx yxyx yxyx tyty ryry "
new_string = ""

for x in orginal_string:
    if x  == "x":
        new_string += "y"
    else:
        new_string += x
print (orginal_string)
print (new_string)
