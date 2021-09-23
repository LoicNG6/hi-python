from random import randint

def get_machine_move():
	return randint(0,2)

def get_result(u_m, m_m):
	if u_m == m_m:
		return 1
	elif u_m == 0 and m_m == 2:
		return 1
	elif u_m == 1 and m_m == 0:
		return 1
	elif u_m == 2 and m_m == 1:
		return 1
	else:
		return 0

user_move = int(input("Put a number between 0 and 2: "))
machine_move = get_machine_move()

while(get_result(user_move, machine_move) == 1):
	print("\n"+"You won." + " Your move : %d  Machine move: %d" %(user_move,machine_move) + "\n")
	user_move = int(input("Put again a number between 0 and 2: "))
	machine_move = get_machine_move()
	get_result(user_move, machine_move)

print("\n"+"Loss. Your move: %d. Machine move: %d" %(user_move,machine_move))