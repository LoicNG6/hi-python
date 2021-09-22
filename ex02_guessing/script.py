from random import randint

inf = int(input("Put a number please: "))
supp = int(input("\n"+"Put a bigger number than the first please: "))
system_nb = randint(inf,supp)
user_nb = int(input("\n"+"Try to find the machine number: "))

while user_nb != system_nb:
	if user_nb < system_nb:
		print("\n"+"too small")
		user_nb = int(input("Retry: "))
	else:
		print("\n"+"too big")
		user_nb = int(input("Retry: "))
	

print("\n"+"Congratulations ! You found the system number.")
print("\n" + "Your response = %d  The sytem number = %d " %(user_nb, system_nb)+"\n")