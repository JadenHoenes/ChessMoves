import random

# the chess piece super class
class ChessPiece:
    def __init__(self,color,x,y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return (self.__x,self.__y)

    def x(self):
        return self.__x
        
    def y(self):
        return self.__y

class Pawn(ChessPiece):
  #Determines color and checks the position above or below for validity
  def validMove(self, x,y):
    if self.color() == 'w':
      if self.x() == x and self.y() + 1 == y:
        return True
    else:
      if self.x() == x and self.y() - 1 == y:
        return True
  
  def pic(self):
    if self.color() == 'w':
      return '\u2659'
    else:
      return '\u265f'

class Queen(ChessPiece):
  #Combines Rook and Bishop logic
  #Checks all positions to check for diagonal positions
  #if so returns True
  #Checks Rows and Columns for validity
  def validMove(self, x,y):
    for i in range(-7,7):
      if (self.x() + i == x and self.y() + i == y) or (self.x() + i == x and self.y() - i == y):
        return True
    if x == self.x() or y == self.y():
      return True
    
  
  def pic(self):
    if self.color() == 'w':
      return '\u2655'
    else:
      return '\u265b'

class King(ChessPiece):
  #Checks surrounding positions using the relative positions that are valid
  def validMove(self, x,y):
    relPos = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(8):
      if self.x() + relPos[i][0] == x and self.y() + relPos[i][1] == y: return True

  
  def pic(self):
    if self.color() == 'w':
      return '\u2654'
    else:
      return '\u265a'

class Bishop(ChessPiece):
  #Checks all positions on board, checks if it's a diagonal
  def validMove(self, x,y):
    for i in range(-7,8):
      if (self.x() + i == x and self.y() + i == y) or (self.x() + i == x and self.y() - i == y):
        return True

  def pic(self):
    if self.color() == 'w':
      return '\u2657'
    else:
      return '\u265d'

class Rook(ChessPiece):
  #Determines if it's in a row or column
  def validMove(self, x,y):
    if x == self.x() or y == self.y():
      return True
    else:
      return False
  
  def pic(self):
    if self.color() == 'w':
      return '\u2656'
    else:
      return '\u265c'

class Knight(ChessPiece):
  #Checks x and y using relative positions to determine validity
  def validMove(self,x,y):
    relPos = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-2,1],[-1,2]]
    for i in range(8):
      if self.x() + relPos[i][0] == x and self.y() + relPos[i][1] == y: return True
  
  def pic(self):
    if self.color() == 'w':
      return '\u2658'
    else:
      return '\u265e'

# print a nice picture of the valid moves 
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ",cp.pic()," at",cp.location())
    for i in range(7,-1,-1):
        print("\t"+str(i)+" ",end="")
        for j in range(0,8):
            if cp.x()==j and cp.y()==i:
                print(cp.pic()+" ",end="")
            elif cp.validMove(j,i):
                print("* ",end="")
            else:
                print(". ",end="")
        print()
    print("\t  ",end="")
    for i in range(0,8):
        print(str(i)+" ",end="")
    print()
    print()

       
# returns a random chess piece at a random location
def randomChessPiece():
    if random.randint(0,1) == 0: c="w"
    else: c="b"
    t = random.randint(1,6)
    x = random.randint(0,7)
    y = random.randint(0,7)
    if t == 1: return Pawn(c,x,y)
    if t == 2: return Queen(c,x,y)
    if t == 3: return King(c,x,y)
    if t == 4: return Rook(c,x,y)
    if t == 5: return Knight(c,x,y)
    else:      return Bishop(c,x,y)


def main():
    clist = []

    # make a list of random chess pieces
    for i in range(0,10):
        clist.append(randomChessPiece())

    # display thier valid moves
    for i in range(0,len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])

main()
