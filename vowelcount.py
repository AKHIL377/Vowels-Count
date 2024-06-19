s = input()
v = "aeiou"
mx = -999 #Stores the maximum count of consecutive vowels encountered so far (initialized to -999, assuming there won't be more than 999 consecutive vowels)
ans = 0 #Stores the character that forms the start of the longest vowel substring (initialized to 0, which is not a valid character)
d = {} #An empty dictionary that will be used to keep track of the count of each vowel encountered.This dictionary contains the count of each vowel encountered in the string.

for i in s:
    if i in v:  # Check if character i is a vowel
        if i not in d:
            d[i] = 1  # Initialize count for the vowel if not seen before
        else:
            d[i] += 1  # Increment count for the current vowel
        if d[i] > mx:  # Update maximum vowel count and corresponding character
            mx = d[i]
            ans = i

print(d)
