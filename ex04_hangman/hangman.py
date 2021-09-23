from research_word import research_word
import random
from random import choice

countrie_names = ['France','Germany','Spain','England','Italia','Belgium','Canada','Usa','Mexico','Brazil','Panama','China','Japan','India','Syria','Egypt','Moroco','Tunisia','Algeira','Liberia','Senegal','Ghana','Nigeria','Mali','Niger','Cameroon','Gabon','Drc','Tanzania']

the_country = random.choice(countrie_names)

if len(the_country) <= 3:
	trials = 3
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	print(research_word(the_country, trials, result))

if len(the_country) > 3 and len(the_country)<=5:
	trials = 5
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	result[len(the_country)-1] = the_country[len(the_country)-1]
	print(research_word(the_country, trials, result))

if len(the_country) > 5:
	trials = 8
	result = ['_' for i in range(len(the_country))]
	result[0] = the_country[0]
	result[len(the_country)//2] = the_country[len(the_country)//2] 
	result[len(the_country)-1] = the_country[len(the_country)-1]
	print(research_word(the_country, trials, result))