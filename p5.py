#Write a Python program that calculates and displays the winning percentage of a team by taking the number of wins, losses and matches drawn by the team.
w=int(input("Enter the Total Number of Games Won by the Team: "))
l=int(input("Enter the Total Number of Games Lost by the Team: "))
d=int(input("Enter the Total Number of Games Drawn by the Team: "))
t=w+l+d
wp=(w/t)*100
print(f"Your Winning Percentage is {wp:.2f}")
