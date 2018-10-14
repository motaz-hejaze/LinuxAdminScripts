print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||                                                                                                                                       ||")
print("||                                      Developed By AlMotaz Hejaze 2/oct/2018 m3tz-hjze@hotmail.com                                     ||")
print("||                                       A script to search for change password BOTS in a log file                                       ||")
print("||                                                                                                                                       ||")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print("\n")

#open the log file using with statement to automaticaly close it 
with open("log.txt","r") as f:
	#some initial values
	temp = 0
	total_bots = []
	logged_in = False
	password_change = False
	total = 0
	bot_name = ''
	#iterating through the file line by line
	for l in f:
		#splitting the line string to an array
		word =  l.split(' ')
		print(word)
		print("\n")
        	time = word[4].split(':')
        	second = time[2]
		phrase = str(word[9])
		bot_name = str(word[5].split("|")[2])
		#checking for the login
        	if phrase == 'in|':
			print(bot_name + " Logged In")
			print("\n")
			#he is logged in now 
                	logged_in = True
                	temp = int(second)
			continue
		#if logged in then checking for password change in the same second 
        	elif logged_in and phrase == 'password|' and temp == int(second):
			print(bot_name + " Changed Password")
			print("\n")
			#he changed password
                	pass_change = True
			continue
		elif logged_in and pass_change and phrase == 'off|' and temp == int(second):
			print(bot_name + " Logged Out")
			print("\n")
                	print("***** A Bot detected *****")
			print("\n")
			#total number of bots detected
                	total = total + 1
			print("We have " + str(total) + " bots")
			print("\n")
			#adding the current bot name to the the total_bots array
                	if bot_name not in total_bots:
				total_bots.append(str(bot_name))
		else:
			print("nothing special")
			print("\n")
			#back to initial state
			in_ = False
			pass_change = False
			continue

print("\n")
print("********* Total Bots Detected are : " + str(total) + " , and there names are : ****************************")
print("\n")
#showing results
for bot in total_bots:
	print(bot)
	print("\n")

#writing results to another file bots_names.txt
with open("bots_names.txt","w") as f:
	for bot in total_bots:
		f.write(bot)
		f.write("\n")

print(" All Bots Names Are written to bots_names.txt file")
print("\n")
print("                          ||||||||||||||||||||||||||End OF File||||||||||||||||||||||||||||||                                        ")
