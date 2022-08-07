fullstring = "StackAbuse"
substring = "tack"

try:
    fullstring.index(substring)
except ValueError:
    print("Not found!")
else:
    print("Found!")
