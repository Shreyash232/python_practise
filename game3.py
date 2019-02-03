p1=input("player 1:")
p2=input("player 2:")

if p1==p2:
	print("its tie")
if p1=="paper":
	if p2=="rock":
		print("p1 wins")
	elif p2=="scissor":
		print("p2 wins")

if p1=="rock":
	if p2=="scissor":
		print("p1 wins")
	elif p2=="paper":
		print("p1 wins")

if p1=="scissor":
	if p2=="paper":
		print("p1 wins")
	elif p2=="rock":
		print("p2 wins")
		





