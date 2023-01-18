# Imports
import PlayerWinner
import PlayerVictor
import PlayerChamption

# Welcome Script
def Welcome():
  print("=================================================================")
  print("Welcome to the dream Basketball Game Bracket!!")
  print("Please start off by entering 8 players that will duke it out!")
  print("=================================================================")

Welcome()

# Player Innitiation
player1 = input("Please enter in player 1: ")
player2 = input("Please enter in player 2: ")
player3 = input("Please enter in player 3: ")
player4 = input("Please enter in player 4: ")
player5 = input("Please enter in player 5: ")
player6 = input("Please enter in player 6: ")
player7 = input("Please enter in player 7: ")
player8 = input("Please enter in player 8: ")

# Wave 1
winner = PlayerWinner.Player1_VS_Player2(player1, player2)
winner2 = PlayerWinner.Player3_VS_Player4(player3, player4)
winner3 = PlayerWinner.Player5_VS_Player6(player5, player6)
winner4 = PlayerWinner.Player7_VS_Player8(player7, player8)
print("Your winners are: ",winner,",",winner2,",",winner3,",",winner4)

# Wave 2
victor = PlayerVictor.Winner1_VS_Winner2(winner, winner2)
victor2 = PlayerVictor.Winner3_VS_Winner4(winner3, winner4)
print("Your victors are: ",victor,",",victor2)

# Champion Stage
champ = PlayerChamption.PlayerChamp(victor, victor2)
print("Your champion is: ", champ)
