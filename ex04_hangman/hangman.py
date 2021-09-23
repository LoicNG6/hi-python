import random
from random import choice


countries = ['France','Germany','Spain','England','Italia','Belgium','Canada','Usa','Mexico','Brazil','Panama','China','Japan','India','Syria','Egypt','Moroco','Tunisia','Algeira','Liberia','Senegal','Ghana','Nigeria','Mali','Niger','Cameroon','Gabon','Drc','Tanzania']

the_country = random.choice(countries)
the_country_temp = the_country

if len(the_country) <= 3:
	trial = 3
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	
	while trial >= 0 :
		print(trial, result)
		user_char = str(input("\n"+"Put a lettre to find the word : "))
		if user_char in the_country:
			result[the_country.index(user_char)] = user_char
			the_country = the_country.replace(user_char, ' ', 1)
		if "".join(result) == the_country_temp:
			print("\n" + "Congratulations ! You found the word: %s" %("".join(result))+ "\n")
			break
		trial -= 1
	
	if "".join(result) == the_country_temp:
		if trial == 0:
			print("\n" + "You found the word at the last moment !" + "\n")
	else:
		print("\n" +"Loss.")


if len(the_country) > 3 and len(the_country)<=5:
	trial = 5
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	result[len(the_country)-1] = the_country[len(the_country)-1]
	
	while trial >= 0 :
		print(trial, result)
		user_char = str(input("\n"+"Put a lettre to find the word : "))
		if user_char in the_country:
			result[the_country.index(user_char)] = user_char
			the_country = the_country.replace(user_char, ' ', 1)
		if "".join(result) == the_country_temp:
			print("\n" + "Congratulations ! You found the word: %s" %("".join(result))+ "\n")
			break	
		trial -= 1

	if "".join(result) == the_country_temp:
		if trial == 0:
			print("\n" + "You found the word at the last moment !" + "\n")
	else:
		print("\n" +"Loss.")


if len(the_country) > 5:
	trial = 8
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	result[len(the_country)//2] = the_country[len(the_country)//2] 
	result[len(the_country)-1] = the_country[len(the_country)-1]
	
	while trial >= 0 :
		print(trial, result)
		user_char = str(input("\n"+"Put a lettre to find the word : "))
		if user_char in the_country:
			result[the_country.index(user_char)] = user_char
			the_country = the_country.replace(user_char, ' ', 1)
		if "".join(result) == the_country_temp:
			print("\n" + "Congratulations ! You found the word: %s" %("".join(result))+ "\n")
			break	
		trial -= 1
	
	if "".join(result) == the_country_temp:
		if trial == 0:
			print("\n" + "You found the word at the last moment !" + "\n")
	else:
		print("\n" +"Loss.")
