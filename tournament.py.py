#Matthew Davis
#Program 6
#10/18/2024
#COP2500C_CMB-24Fall 00139

import math

divisions=0

# Ask user for input for divisins
divisions=int(input("How many divisions are in the tournament?\n"))

# Set starting to one, add to division for each input
for i in range(1, divisions+1):

    # Ask user for player input
    print("How many players are in Division ",i,"?",sep="")
    players = int(input())

    # Setting besttime to a large number to calculate
    # So it can find the lowest number
    besttime=float(5000)

    # Nested For Loop
    for j in range(1, players+1):

        # Ask user for the time of each player in a division
        print("What was the time of Player #",j,"?",sep="")
        time = int(input())

        # Calculate to see if the lowest time is greater than
        # the float bestime set
        if time < besttime:
            besttime=time
            
    # Calculate for Average Time
    averagetime=time/players

    # Print statements that are outputted after each division is finished.
    print("Division #",i," Results:",sep="")
    print("Best Time:",besttime,"seconds")
    print("Average Time:", "%.1f"%averagetime,"seconds")
