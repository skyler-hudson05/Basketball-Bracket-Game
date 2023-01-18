# Imports
import time
import random


# Player bracket to find champion
def PlayerChamp(victor, victor2):
  print("-------------------------------------------------")
  print("Moving onto the final stage, finding the champ!")
  print("-------------------------------------------------")

  # Tracking player score
  victorScore = 0
  victor2Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(victor, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      victorScore += 1
      print("He got a one point shot. Score is now: ", victorScore)
    if(randomPointer == 2):
      victorScore += 2
      print("He got a two points. Score is now: ", victorScore)
    if(randomPointer == 3):
      victorScore += 3
      print("HE SCORES 3 POINTS!! Score is now: ", victorScore)

  print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(victor2, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      victor2Score += 1
      print("He got a one point shot. Score is now: ", victor2Score)
    if(randomPointer == 2):
      victor2Score += 2
      print("He got a two points. Score is now: ", victor2Score)
    if(randomPointer == 3):
      victor2Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", victor2Score)

  # Calculating the winner
  if(victorScore > victor2Score):
    champ = victor
    print(champ, " has beat ", victor2, ", So ", champ, " moves forward")
    return champ
  elif(victor2Score > victorScore):
    champ = victor2
    print(champ," has beat ",victor,", So ",champ," moves forward")
    return victor
  elif(victorScore == victor2Score or victor2Score == victorScore):
    coinToss = random.randrange(1,2)
    player1Input = input("Heads or Tails? ")
    player2Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player1Input == "Heads" and coinToss == 1):
      champ = victor
      print(victor, " has won this event")
      return champ
    elif(player1Input == "Tails" and coinToss == 2):
      champ = victor
      print(victor, " has won this event")
      return champ

    if(player2Input == "Heads" and coinToss == 1):
      champ = victor2
      print(victor2, " has won this event")
      return champ
    elif(player1Input == "Tails" and coinToss == 2):
      champ = victor2
      print(victor2, " has won this event")
      return champ
