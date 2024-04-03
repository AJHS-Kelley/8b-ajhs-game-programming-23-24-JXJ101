alphabet = "abcdefghijklmnopqrstuvwxyz"
myString = "Type a random string with punctuation, please.\n"

print(alphabet[0])
print(alphabet[-1])

# Slicing
print(alphabet[0:4]) # Slice UP TO second index.
# alphabet[start:stop]

# Slice from the start
print(alphabet[:7])

# Slice to the end
print(alphabet[12:])

# Slice the Whole *$^% Thing
print(alphabet[:])

# Negative Index slicing
print(alphabet[-4:-1])

print(myString[26:-10])