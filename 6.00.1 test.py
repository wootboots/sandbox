s = 'azcbobobegghakl'

maxlength = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
	if s[i+1] >= s[i]:
		current += s[i+1]
		if len(current) > maxlength:
			maxlength = len(current)
			longest = current
	else:
		current = s[i+1]
	i += 1
    
print("The longest substring in alphabetical order is: " + longest)