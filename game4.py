p1=input("player 1:").lower()
print("*****NO CHEATING...\n\n"*40)
p2=input("player 2:").lower()

if p1=="rock" or p1=="paper" or p1=="scissor":
	if p1==p2:
		print("its tie")

	if p1=="paper":
		if p2=="rock":
			print("p1 wins")
		elif p2=="scissor":
			print("p2 wins")
		else :
			print("invalid input")

	if p1=="rock":
		if p2=="scissor":
			print("p1 wins")
		elif p2=="paper":
			print("p1 wins")
		else:
			print("invalid input")


	if p1=="scissor":
		if p2=="paper":
			print("p1 wins")
		elif p2=="rock":
			print("p2 wins")
		else:
			print("invalid input")

else:
	print("oops something went wrong")


