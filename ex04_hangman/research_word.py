
def research_word(country, trials, user_word):
	country_temp = country

	while trials >= 0 :
		print(trials, user_word)
		user_char = str(input("\n"+"Put a lettre to find the word : "))
		if user_char in country_temp and user_char != '':
			user_word[country_temp.index(user_char)] = user_char
			country_temp = country_temp.replace(user_char, ' ', 1)
		if "".join(user_word) == country:

			print("\n" + "Congratulations ! You found the word: %s" %("".join(user_word))+ "\n")
			break
		trials -= 1

	if "".join(user_word) == country:
		return "You found the word at the last moment !" + "\n" if trials == 0 else ""
	else:
		return "\n" + "You lost. The word was: "+ country + "\n"