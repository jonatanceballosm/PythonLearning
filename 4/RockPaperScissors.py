import random as rand

class RockPaperScissor:

    def __init__(self) -> None:
        self.ROCK = self.rock()
        self.SCIS = self.scissor()
        self.PAPER = self.paper()

    def play(self):
        print("Welcome to Rock, Paper Scissor!\n")
        keep_playing = True
        while(keep_playing):
            print("Please enter your choice.")
            player_choice = self.selection(False)
            computer_choice = self.selection(str(rand.randint(1,3)))

            self.result(player_choice, computer_choice)
            while(keep_playing):
                try:
                    answer = input("Replay? (Y)es or (N)o: ")

                    if (answer[0].lower() == 'n'):
                        keep_playing = False
                    elif (answer[0].lower() != 'y'):
                        raise ValueError("Please enter only (Y)es or (N)o.")
                    else:
                        break
                except ValueError as ve:
                    print(ve)




    def selection(self,computer):
        valid_entry = False
        while(not valid_entry):
                  if(not computer):
                    response = input("Choose between (R)ock, (P)aper or (S)cissor: ")
                  else:
                     response = computer

                  letter = response[0].lower()
                  try:
                    if (letter == 'r' or letter == '1'):
                      response = self.rock()
                      valid_entry = True
                    elif (letter == 'p' or letter == '3'):
                      response = self.paper()
                      valid_entry = True
                    elif (letter == 's' or letter == '2'):
                      response = self.scissor()
                      valid_entry = True
                    else:
                      raise ValueError("Invalid input. Please select (R)ock, (P)aper or (S)cissor!")
                  except ValueError as ve:
                    print(ve)
                  else:
                     return response

    def result(self, player_choice, computer_choice):
        if((player_choice[0] == 1 and computer_choice[0] == 2) or 
           (player_choice[0] == 2 and computer_choice[0] == 3) or
           (player_choice[0] == 3 and computer_choice[0] == 1)):
           print("*****You win!*****")
           print("You played: " + player_choice[1])
           print("*****VS*****")
           print("Computer played: " + computer_choice[1])
        elif player_choice[0] == computer_choice[0]:
            print("*****Tie!*****")
            print("You played: " + player_choice[1])
            print("VS")
            print("Computer played: " + computer_choice[1])
        else:
            print("*****You lose!*****")
            print("You played: " + player_choice[1])
            print("*****VS*****")
            print("Computer played: " + computer_choice[1])


    def rock(self):
        return 1, '''
               ,--.--._
        ------" _, \___)
                / _/____)
                \//(____)
        ------\     (__)
               `-----"
            '''
    def scissor(self):
        return 2, '''
       _    (^)
      (_\   |_|
       \_\  |_|
       _\_\,/_|
      (`\(_|`\|
     (`\,)  \ \\
      \,)   | |     
        \__(__|
        '''    
    def paper(self):
        return 3, '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
          '''

new_game = RockPaperScissor()
new_game.play()