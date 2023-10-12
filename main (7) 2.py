# Define the base class player 
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the deived class Batsman
class Batsman(Player):
    def play(self):
        print ("The batsman is batting.")

# Define the deribed class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()