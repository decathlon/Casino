# blackjack.py

from random import shuffle

faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace" )
suits = ( "Clubs", "Diamonds", "Hearts", "Spades" )
values = ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 )

class Card:

   def __init__( self, face, suit, value ):
      self.face = face
      self.suit = suit
      self.value = value

class Deck:

   def __init__( self, numDecks ):
      self.topCard = 0
      self.deck = []
      for k in range( 0, numDecks ):
         for i in range( 0, len( suits ) ):
            for j in range( 0, len( faces ) ):
               self.deck.append( Card( faces[j], suits[i], values[j] ) )

   def shuffleDeck( self ):
      shuffle( self.deck )

   def dispDeck( self, start, stop ):
      for i in range( start, stop ):
         print( self.deck[ i ].face, " of ", self.deck[ i ].suit )

   def setTopCard( self, top ):
      self.topCard = top

   def getTopCard( ):
      return topCard

class Hand:

   def __init__( self ):
      self.score = 0
      self.hand = []
      self.scoreList = []

   def countAces( self ):
      numAces = 0
      for i in range( 0, len( self.hand ) ):
         if self.hand[ i ].face == "Ace":
            numAces += 1
      return numAces
   
   def scoreHand( self ):
      self.score = 0
      for i in range( 0, len( self.hand ) ):
         self.score += self.hand[ i ].value

   def acesScoring( self ):
      a = self.countAces( )
      for i in range( 0, a + 1 ):
         if len( self.scoreList ) == i :
            self.scoreList.append( self.score - i * 10 )
         else:
            self.scoreList[ i ] = self.score - i * 10

#      if a == 0:
#         if len( self.scoreList ) == 0:
#            self.scoreList.append( self.score )
#         else:
#            self.scoreList[0] = self.score
#      else:
#         for i in range( 0, a + 1 ):
#            if len( self.scoreList ) == i :
#               self.scoreList.append( self.score - i * 10 )
#            else:
#               self.scoreList[ i ] = self.score - i * 10
      
      self. score = self.scoreList[ len( self.scoreList ) - 1 ]
#      for i in range( len( self.scoreList ), 0 ):
      for i in range( len( self.scoreList ), -1 ):
         if self.scoreList[ i ] <= 21:
            self. score = self.scoreList[ i ]
            

   def dispScore( self ):
      for i in range( 0, len( self.scoreList ) ):
         print( self.scoreList[ i ], " ", end="" )
      print( '\n' )

   def dispHand( self ):
      for i in range( 0 , len( self.hand ) ):
         print( "%s%s%s" % ( self.hand[i].face.rjust(5), " of ", self.hand[i].suit.ljust(8) ) )

   def dispDealerHand( self ):
      print( self.hand[0].face, " of ", self.hand[0].suit )
      print( "FACEDOWN" )

class Player:

   def __init__( self, name, stash ):
      self.playerHand = Hand( )
      self.name = name
      self.pocket = stash

   def newHand( self, newHand ):
      self.playerHand = newHand

   def placeBet( self, betAmount ):
      self.pocket -= betAmount

   def winBet( self, winAmount ):
      self.pocket += winAmount

class Game:

   def __init__( self, playerx, playery ):
      self.player = playerx
      self.dealer = playery

   def initialDeal( self, deckx ):
      for i in range( deckx.topCard, deckx.topCard + 4, 2 ): #0, 4, 2 ):
         self.player.playerHand.hand.append( deckx.deck[ i ] )
         self.dealer.playerHand.hand.append( deckx.deck[ i + 1 ] )
      deckx.setTopCard( i + 2 )

   def hit( self, playerx, deckx ):
      playerx.playerHand.hand.append( deckx.deck[ deckx.topCard ] )
      deckx.setTopCard( deckx.topCard + 1 )

   def playerInput( self ):
      a = "x"
      while a.upper() != "H" and a.upper() != "S" :
         a = input( "Hit or Stand? enter H or S -> " )
         a.upper()
      return a.upper()

   def playAgain( self ):
      a = "x"
      while a.upper() != "N" and a.upper() != "Y" :
         a = input( "Play another hand? enter Y or N -> " )
         a.upper()
      return a.upper()


def main():
#   print( "In Main\n" )

   numDecks = eval( input( "Enter number of decks to play with -> " ) )

   newDeck = Deck( numDecks )
   newDeck.shuffleDeck( )
#   newDeck.dispDeck( 0, 16 )

   player = Player( "Adam", 1000 )
   dealer = Player( "Dealer", 10000 )


   newGame = Game( player, dealer)

   play = "Y"
   while play == "Y" and newDeck.topCard < ( numDecks * ( 52 - 20 ) ):
      action = " "
      newGame.initialDeal( newDeck )

      print( '\n', newGame.player.name )
      player.playerHand.dispHand( )
      player.playerHand.scoreHand( )
      player.playerHand.acesScoring( )
      player.playerHand.dispScore( )

      print( '\n', newGame.dealer.name )
      dealer.playerHand.dispDealerHand( )

      print( '\n', newGame.player.name )

      if player.playerHand.score == 21:
         print( '\n', newGame.player.name, "Blackjack!", '\n' )
      else:
         action = newGame.playerInput( )
         while action == "H" and player.playerHand.score <= 20:
            newGame.hit( player, newDeck )
            player.playerHand.dispHand( )
            player.playerHand.scoreHand( )
            player.playerHand.acesScoring( )
            player.playerHand.dispScore( )
            if player.playerHand.score < 21:
               action = newGame.playerInput( )
            if player.playerHand.score > 21:
               print( '\n', newGame.player.name, "Busted!", '\n' )

      print( '\n', newGame.dealer.name )
      dealer.playerHand.dispHand( )
      dealer.playerHand.scoreHand( )
      dealer.playerHand.acesScoring( )
      dealer.playerHand.dispScore( )
   
      if player.playerHand.score > 21:
         print( '\n', newGame.player.name, "Busted!", '\n' )
         print( '\n', newGame.dealer.name, " Wins!", '\n' )
      elif dealer.playerHand.score == 21 and player.playerHand.score == 21:
         print( '\n', newGame.dealer.name, "Blackjack!", '\n' )
         if player.playerHand.score == 21:
            print( '\n', "Push - ", newGame.player.name, "'s bet returned", '\n' )
      else:
         while dealer.playerHand.score < 16:
            newGame.hit( dealer, newDeck )
            dealer.playerHand.dispHand( )
            dealer.playerHand.scoreHand( )
            dealer.playerHand.acesScoring( )
            dealer.playerHand.dispScore( )
            if dealer.playerHand.score > 21:
               print( '\n', newGame.dealer.name, "Busted!", '\n' )
               print( newGame.player.name, " Wins!" )
         if player.playerHand.score <= 21  and dealer.playerHand.score <= 21:
            if player.playerHand.score <= dealer.playerHand.score:
               print( newGame.dealer.name, " Wins", '\n' )
            else:
               print( newGame.player.name, " Wins!" )
      
      play = newGame.playAgain( )
      if play == "Y":
         hand1 = Hand( )
         hand2 = Hand( )
         newGame.player.playerHand = hand1
         newGame.dealer.playerHand = hand2

   print( "Not enough cards are left in the deck to play another hand" )

main()
