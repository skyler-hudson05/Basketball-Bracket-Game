# Imports
import time
import random

# Player bracket to find victor

def Winner1_VS_Winner2(winner, winner2):
  print("-------------------------------------------------")
  print("Moving onto the next stage, finding the victor!")
  print("-------------------------------------------------")

  # Tracking player score
  winnerScore = 0
  winner2Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(winner, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      winnerScore += 1
      print("He got a one point shot. Score is now: ", winnerScore)
    if(randomPointer == 2):
      winnerScore += 2
      print("He got a two points. Score is now: ", winnerScore)
    if(randomPointer == 3):
      winnerScore += 3
      print("HE SCORES 3 POINTS!! Score is now: ", winnerScore)

  print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(winner2, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      winner2Score += 1
      print("He got a one point shot. Score is now: ", winner2Score)
    if(randomPointer == 2):
      winner2Score += 2
      print("He got a two points. Score is now: ", winner2Score)
    if(randomPointer == 3):
      winner2Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", winner2Score)

  # Calculating the winner
  if(winnerScore > winner2Score):
    victor = winner
    print(victor, " has beat ", winner2, ", So ", victor, " moves forward")
    return victor
  elif(winner2Score > winnerScore):
    victor = winner2
    print(victor," has beat ",winner,", So ",victor," moves forward")
    return victor
  elif(winnerScore == winner2Score or winner2Score == winnerScore):
    coinToss = random.randrange(1,2)
    player1Input = input("Heads or Tails? ")
    player2Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player1Input == "Heads" and coinToss == 1):
      victor = winner
      print(winner, " has won this event")
      return victor
    elif(player1Input == "Tails" and coinToss == 2):
      victor = winner
      print(winner, " has won this event")
      return victor

    if(player2Input == "Heads" and coinToss == 1):
      victor = winner2
      print(winner2, " has won this event")
      return victor
    elif(player2Input == "Tails" and coinToss == 2):
      victor = winner2
      print(winner2, " has won this event")
      return victor

  print("========================================")


def Winner3_VS_Winner4(winner3, winner4):

  # Tracking player score
  winner3Score = 0
  winner4Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(winner3, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      winner3Score += 1
      print("He got a one point shot. Score is now: ", winner3Score)
    if(randomPointer == 2):
      winner3Score += 2
      print("He got a two points. Score is now: ", winner3Score)
    if(randomPointer == 3):
      winner3Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", winner3Score)

  print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(winner4, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      winner4Score += 1
      print("He got a one point shot. Score is now: ", winner4Score)
    if(randomPointer == 2):
      winner4Score += 2
      print("He got a two points. Score is now: ", winner4Score)
    if(randomPointer == 3):
      winner4Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", winner4Score)

  # Calculating the winner
  if(winner3Score > winner4Score):
    victor2 = winner3
    print(victor2, " has beat ", winner4, ", So ", victor2, " moves forward")
    return victor2
  elif(winner4Score > winner3Score):
    victor2 = winner4
    print(victor2," has beat ",winner3,", So ",victor2," moves forward")
    return victor2
  elif(winner3Score == winner4Score or winner4Score == winner3Score):
    coinToss = random.randrange(1,2)
    player1Input = input("Heads or Tails? ")
    player2Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player1Input == "Heads" and coinToss == 1):
      victor = winner3
      print(winner3, " has won this event")
      return victor
    elif(player1Input == "Tails" and coinToss == 2):
      victor = winner3
      print(winner3, " has won this event")
      return victor

    if(player2Input == "Heads" and coinToss == 1):
      victor = winner4
      print(winner4, " has won this event")
      return victor
    elif(player2Input == "Tails" and coinToss == 2):
      victor = winner4
      print(winner4, " has won this event")
      return victor

  print("========================================")
