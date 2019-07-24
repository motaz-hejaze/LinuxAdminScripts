def longest_substring_without_repeat(string):
	substring = ''
	max_substring_length = 0
	for i in range(len(string)):
		x = string[i]
		if x in substring:
			if len(substring) > max_substring_length:
				max_substring_length = len(substring)
			substring = ''
			substring += x		
		else:
			substring += x			
	print("Max substring length in " + string + " is : " + str(max_substring_length))
	
		


longest_substring_without_repeat("abcabcabcxxxx")
longest_substring_without_repeat("hoxddhoxxdhohoxxd")
longest_substring_without_repeat("bbbbbb")
longest_substring_without_repeat("abcabcbb")
