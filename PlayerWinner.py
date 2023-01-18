# Imports
import time
import random


# Player Bracket to find winner
def Player1_VS_Player2(player1, player2):

  # Tracking player score
  player1Score = 0
  player2Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player1, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player1Score += 1
      print("He got a one point shot. Score is now: ", player1Score)
    if(randomPointer == 2):
      player1Score += 2
      print("He got a two points. Score is now: ", player1Score)
    if(randomPointer == 3):
      player1Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player1Score)
    elif(player1Score == player2Score or player2Score == player1Score):
      coinToss = random.randrange(1,2)
      player1Input = input("Heads or Tails? ")
      player2Input = input("Heads or Tails? ")

      # Coin Toss Tie Breaker
      if(player1Input == "Heads" and coinToss == 1):
        winner = player1
        print(player1, " has won this event")
        return winner
      elif(player1Input == "Tails" and coinToss == 2):
        winner = player1
        print(player1, " has won this event")
        return winner

      if(player2Input == "Heads" and coinToss == 1):
        winner = player2
        print(player2, " has won this event")
        return winner
      elif(player2Input == "Tails" and coinToss == 2):
        winner = player2
        print(player2, " has won this event")
      return winner
    

  print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player2, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player2Score += 1
      print("He got a one point shot. Score is now: ", player2Score)
    if(randomPointer == 2):
      player2Score += 2
      print("He got a two points. Score is now: ", player2Score)
    if(randomPointer == 3):
      player2Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player2Score)

  # Calculating the winner
  if(player1Score > player2Score):
    winner = player1
    print(winner, " has beat ", player2, ", So ", winner, " moves forward")
    return winner
  elif(player2Score > player1Score):
    winner = player2
    print(winner," has beat ",player1,", So ",winner," moves forward")
    return winner
  elif(player1Score == player2Score or player2Score == player1Score):
    coinToss = random.randrange(1,2)
    player1Input = input("Heads or Tails? ")
    player2Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player1Input == "Heads" and coinToss == 1):
      winner = player1
      print(player1, " has won this event")
      return winner
    elif(player1Input == "Tails" and coinToss == 2):
      winner = player1
      print(player1, " has won this event")
      return winner

    if(player2Input == "Heads" and coinToss == 1):
      winner = player2
      print(player2, " has won this event")
      return winner
    elif(player2Input == "Tails" and coinToss == 2):
      winner = player2
      print(player2, " has won this event")
      return winner

  print("========================================")


def Player3_VS_Player4(player3, player4):

  # Tracking player score
  player3Score = 0
  player4Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player3, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player3Score += 1
      print("He got a one point shot. Score is now: ", player3Score)
    if(randomPointer == 2):
      player3Score += 2
      print("He got a two points. Score is now: ", player3Score)
    if(randomPointer == 3):
      player3Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player3Score)

    print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player4, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player4Score += 1
      print("He got a one point shot. Score is now: ", player4Score)
    if(randomPointer == 2):
      player4Score += 2
      print("He got a two points. Score is now: ", player4Score)
    if(randomPointer == 3):
      player4Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player4Score)

  # Calculating the winner
  if(player3Score > player4Score):
    winner2 = player3
    print(winner2, " has beat ", player4, ", So ", winner2, " moves forward")
    return winner2
  elif(player4Score > player3Score):
    winner2 = player4
    print(winner2," has beat ",player3,", So ",winner2," moves forward")
    return winner2
  elif(player3Score == player4Score or player4Score == player3Score):
    coinToss = random.randrange(1,2)
    player3Input = input("Heads or Tails? ")
    player4Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player3Input == "Heads" and coinToss == 1):
      winner2 = player3
      print(player3, " has won this event")
      return winner2
    elif(player3Input == "Tails" and coinToss == 2):
      winner2 = player3
      print(player3, " has won this event")
      return winner2

    if(player4Input == "Heads" and coinToss == 1):
      winner2 = player4
      print(player4, " has won this event")
      return winner2
    elif(player4Input == "Tails" and coinToss == 2):
      winner2 = player4
      print(player4, " has won this event")
      return winner2
  
  print("========================================")


def Player5_VS_Player6(player5, player6):

  # Tracking player score
  player5Score = 0
  player6Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player5, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player5Score += 1
      print("He got a one point shot. Score is now: ", player5Score)
    if(randomPointer == 2):
      player5Score += 2
      print("He got a two points. Score is now: ", player5Score)
    if(randomPointer == 3):
      player5Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player5Score)

    print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player6, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player6Score += 1
      print("He got a one point shot. Score is now: ", player6Score)
    if(randomPointer == 2):
      player6Score += 2
      print("He got a two points. Score is now: ", player6Score)
    if(randomPointer == 3):
      player6Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player6Score)

  # Calculating the winner
  if(player5Score > player6Score):
    winner3 = player5
    print(winner3, " has beat ", player5, ", So ", winner3, " moves forward")
    return winner3
  elif(player6Score > player5Score):
    winner3 = player6
    print(winner3," has beat ",player5,", So ",winner3," moves forward")
    return winner3
  elif(player5Score == player6Score or player6Score == player5Score):
    coinToss = random.randrange(1,2)
    player5Input = input("Heads or Tails? ")
    player6Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player5Input == "Heads" and coinToss == 1):
      winner3 = player5
      print(player5, " has won this event")
      return winner3
    elif(player5Input == "Tails" and coinToss == 2):
      winner3 = player5
      print(player5, " has won this event")
      return winner3

    if(player6Input == "Heads" and coinToss == 1):
      winner3 = player6
      print(player6, " has won this event")
      return winner3
    elif(player6Input == "Tails" and coinToss == 2):
      winner3 = player6
      print(player6, " has won this event")
      return winner3
      
    print("========================================")


def Player7_VS_Player8(player7, player8):

  # Tracking player score
  player7Score = 0
  player8Score = 0

  # Calculating Player 1's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player7, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player7Score += 1
      print("He got a one point shot. Score is now: ", player7Score)
    if(randomPointer == 2):
      player7Score += 2
      print("He got a two points. Score is now: ", player7Score)
    if(randomPointer == 3):
      player7Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player7Score)

    print("//////") 

    # Calculating Player 2's points
  for i in range(3):
    randomPointer = random.randrange(1, 3) # Randomnly chooses if the player shoots a 1, 2, or 3 pointer
    print(player8, " takes the shot...")
    time.sleep(2)
    if(randomPointer == 1):
      player8Score += 1
      print("He got a one point shot. Score is now: ", player8Score)
    if(randomPointer == 2):
      player8Score += 2
      print("He got a two points. Score is now: ", player8Score)
    if(randomPointer == 3):
      player8Score += 3
      print("HE SCORES 3 POINTS!! Score is now: ", player8Score)

  # Calculating the winner
  if(player7Score > player8Score):
    winner4 = player7
    print(winner4, " has beat ", player8, ", So ", winner4, " moves forward")
    return winner4
  elif(player8Score > player7Score):
    winner4 = player8
    print(winner4," has beat ",player7,", So ",winner4," moves forward")
    return winner4
  elif(player7Score == player8Score or player8Score == player7Score):
    coinToss = random.randrange(1,2)
    player7Input = input("Heads or Tails? ")
    player8Input = input("Heads or Tails? ")

    # Coin Toss Tie Breaker
    if(player7Input == "Heads" and coinToss == 1):
      winner4 = player7
      print(player7, " has won this event")
      return winner4
    elif(player7Input == "Tails" and coinToss == 2):
      winner4 = player7
      print(player7, " has won this event")
      return winner4

    if(player8Input == "Heads" and coinToss == 1):
      winner4 = player8
      print(player8, " has won this event")
      return winner4
    elif(player8Input == "Tails" and coinToss == 2):
      winner4 = player8
      print(player8, " has won this event")
      return winner4
  print("========================================")

