p1=input("player 1:")
p2=input("player 2:")


if p1=="rock" and p2=="paper":
	print("player2 wins")

elif p1=="rock" and p2=="scissor":
	print("player1 wins")

elif p1=="rock"	and p2=="rock":
	print("its draw")

elif p1=="paper" and p2=="rock":
	print("player1 wins")

elif p1=="paper"and p2=="scissor":
	print("player2wins")

elif p1=="paper" and p2=="paper":
	print("its draw")

elif p1=="scissor" and p2=="paper":
	print("player1 wins")

elif p1=="scissor"	and p2=="rock":
	print("player2 wins")

elif p1=="scissor" and p2=="scissor":
	print("its draw")


