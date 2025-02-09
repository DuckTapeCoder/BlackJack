#Setup
import random

#Declare and Initialize Variables
dealcards = []
dealcards_hidden = []
dealtotal = 0
playercards = []
playertotal = 0
remcards = ["A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K"]
count = 0
count2 = 0
acheck = False
count3 = 0
playerblackjack = False
dealerblackjack = False
stand = False
bust = False
dealerbust = False

#Start Game with opening hand
count = count +  1
number = random.randint(1,len(remcards))
playercards.append(remcards[number - 1])
remcards.remove(playercards[count-1])
draw = playercards[count - 1]
if draw == "J":
  draw = 10
if draw == "Q":
  draw = 10
if draw == "K":
  draw = 10
if draw == "A":
  draw = 11
draw = int(draw)
playertotal = playertotal + draw
print("You drew a " + playercards[count - 1])
print("Your Cards:")
print(playercards)
print("Your total is " + str(playertotal))

count2 = count2 + 1
number = random.randint(1, len(remcards))
dealcards_hidden.append(remcards[number - 1])
remcards.remove(dealcards_hidden[count2 - 1])
draw = dealcards_hidden[count2 - 1]
if draw == "J":
  draw = 10
if draw == "Q":
  draw = 10
if draw == "K":
  draw = 10
if draw == "A":
  draw = 11
draw = int(draw)
dealtotal = dealtotal + draw
print()
print()
print("Dealers Cards:")
dealcards.append("[]")
print(dealcards)

count = count +  1
number = random.randint(1,len(remcards))
playercards.append(remcards[number - 1])
remcards.remove(playercards[count-1])
draw = playercards[count - 1]
if draw == "J":
  draw = 10
if draw == "Q":
  draw = 10
if draw == "K":
  draw = 10
if draw == "A":
  draw = 11
draw = int(draw)
playertotal = playertotal + draw
if playertotal > 21:
  if "A" in playercards:
    while acheck == False:
      while count3 <= count:
        count3 = count3 + 1
        if playercards[count3 - 1] == "A":
          playertotal = playertotal - 10
          playercards[count3 - 1] = "a"
          count3 = 100
          acheck = True
print()
print()
print("You drew a " + playercards[count - 1])
print("Your Cards:")
print(playercards)
print("Your total is " + str(playertotal))
if playertotal == 21:
  print("You Got Black Jack")
  playerblackjack = True


count2 = count2 + 1
number = random.randint(1, len(remcards))
dealcards.append(remcards[number - 1])
remcards.remove(dealcards[count2 - 1])
draw = dealcards[count2 - 1]
if draw == "J":
  draw = 10
if draw == "Q":
  draw = 10
if draw == "K":
  draw = 10
if draw == "A":
  draw = 11
draw = int(draw)
dealtotal = dealtotal + draw
count3 = 0
acheck = False
if dealtotal > 21:
  count3 = 0
  if "A" in dealcards:
    while acheck == False:
      while count3 <= count:
        count3 = count3 + 1
        if dealcards[count3 - 1] == "A":
          dealtotal = dealtotal - 10
          dealcards[count3 - 1] = "a"
          count3 = 100
          acheck = True
print()
print()
print("Dealers Cards:")
print(dealcards)
print("The dealer is showing a " + str(draw))
if dealtotal == 21:
  dealcards[0] = dealcards_hidden[0]
  print()
  print("Dealer Got Black Jack")
  dealerblackjack = True

#Start rest of game with stand and hit
valid = False
playercards2 = playercards
if playercards2[0] == "J":
  playercards2[0] = "10"
if playercards2[0] == "Q":
  playercards2[0] = "10"
if playercards2[0] == "K":
  playercards2[0] = "10"
if playercards2[1] == "J":
  playercards2[1] = "10"
if playercards2[1] == "Q":
  playercards2[1] = "10"
if playercards2[1] == "K":
  playercards2 = "10"

if not playerblackjack:
  if not dealerblackjack:
    print()
    print()
    print("Your Cards:")
    print(playercards)
    print("Your total is " + str(playertotal))
    while not valid:
      print("Please select one of the following:     Hit     Stand")
      hss = input()
      hss = hss.lower()
      if hss != "hit":
        if hss != "stand":
           print("Please input a valid option")
        else:
          valid = True
      else:
        valid = True
#Just selected Hit Stand or Split
    while not stand:
      if hss == "stand":
        stand = True
      elif playertotal >= 21:
        stand = True
        bust = True
      elif hss == "hit":
        count = count +  1
        number = random.randint(1,len(remcards))
        playercards.append(remcards[number - 1])
        remcards.remove(playercards[count-1])
        draw = playercards[count - 1]
        if draw == "J":
          draw = 10
        if draw == "Q":
          draw = 10
        if draw == "K":
          draw = 10
        if draw == "A":
          draw = 11
        acheck = False
        draw = int(draw)
        playertotal = playertotal + draw
        if playertotal > 21:
          if "A" in playercards:
            while acheck == False:
              while count3 <= count:
                count3 = count3 + 1
                if playercards[count3 - 1] == "A":
                  playertotal = playertotal - 10
                  playercards[count3 - 1] = "a"
                  count3 = 100
                  acheck = True
              acheck = True
          else:
            stand = True
        print()
        print()
        print("You drew a " + playercards[count - 1])
        print("Your Cards:")
        print(playercards)
        print("Your total is " + str(playertotal))
        if playertotal > 21:
          print("Bust")
          bust = True
        valid = False
        if playertotal <= 21:
          while not valid:
            print("Please select one of the following:     Hit     Stand")
            hss = input()
            hss = hss.lower()
            if hss != "hit":
              if hss != "stand":
                print("Please input a valid option")
              else:
                valid = True
            else:
              valid = True
if not dealerblackjack:
  if not playerblackjack:
    dealcards[0] = dealcards_hidden[0]
    print()
    print()
    print("Dealers Cards:")
    print(dealcards)
    print("The dealers total is " + str(dealtotal))
    if not bust:
      while dealtotal < 17:
        count2 = count2 + 1
        number = random.randint(1, len(remcards))
        dealcards.append(remcards[number - 1])
        remcards.remove(dealcards[count2 - 1])
        draw = dealcards[count2 - 1]
        if draw == "J":
          draw = 10
        if draw == "Q":
          draw = 10
        if draw == "K":
          draw = 10
        if draw == "A":
          draw = 11
        draw = int(draw)
        dealtotal = dealtotal + draw
        count3 = 0
        acheck = False
        if dealtotal > 21:
          count3 = 0
          if "A" in dealcards:
            while acheck == False:
              while count3 <= count:
                count3 = count3 + 1
                if dealcards[count3 - 1] == "A":
                  dealtotal = dealtotal - 10
                  dealcards[count3 - 1] = "a"
                  count3 = 100
                  acheck = True
        print()
        print()
        print("Dealers Cards:")
        print(dealcards)
        print("The dealers total is " + str(dealtotal))
        if dealtotal > 21:
          print("Dealer Bust")
          dealerbust = True

#Output winner
print()
print()
if bust:
  print("Dealer Wins")
elif dealerbust:
  print("You Win")
elif playerblackjack:
  if dealerblackjack:
    print("Push")
  elif not dealerblackjack:
    print("You Win")
elif dealerblackjack:
  if not playerblackjack:
    print("Dealer Wins")
elif playertotal > dealtotal:
  print("You Win")
  wl = "W"
elif playertotal < dealtotal:
  print("Dealer Wins")
  wl = "L"
elif playertotal == dealtotal:
  print("Push")


  input()