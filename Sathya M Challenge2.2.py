class Player:
  def play(self):
    print("The player is playing cricket.")
class Batsman(Player):
  def play(self):
    print("The batsman is bating.")
class Bowler(Player):
  def play(self):
    print("The bowlwr is bowling.")
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()