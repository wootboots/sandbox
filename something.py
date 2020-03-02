s = 'abcdefghib'
# initialise tracker variables
maxLen = 0
current = s[0] # a
longest = s[0] # a
# step through s indices
# len(s) === 3
# print(len(s))
# len(s) - 1 === 2
# range(len(s) - 1) === [0, 1, 2]
something = range(len(s) - 1)
print(something)
####
# range returns the range 0, 1, 2 of a integer, but stop(the last value is excluded from the range)
###
# for i in range(len(s) - 1): # start at zero and work your way through each character until you get to the last one (range-1 because we started at 0 instead 1)
things = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# start at zero and work your way through each character until you get to the last one (range-1 because we started at 0 instead 1)
for i in things:
# print(s[i + 1])
# i = 0
# i = 1
# i = 2
if s[i + 1] >= s[i]: # is the character following the current character later in the alphabet
# if it is
current += s[i + 1] # current has the next character appended to it
# if current length is bigger update
if len(current) > maxLen: # we have a new maxLen
maxLen = len(current) # assign it to the length of the current
# we assign the current string to the longest getting the longest substring in alpha
longest = current
else: # the next char was not later in the alphabet
# we hit the end of chars in order and we're not at an earlier char in the alphabet
current = s[i + 1]
i += 1 # increment the index
# implied that we keep looping until i reaches the upper bound
print('Longest substring in alphabetical order is: ' + longest)