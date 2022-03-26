import random
import os
import time

#Making a function for clearing the terminal
def clear():
    os.system('cls')

#Making a function in english to print instructions for the game
def en_udinstructions():
    print()
    print("UP-DOWN GAME INSTRUCTIONS")
    print()
    print("YOU HAVE TO FIND THE NUMBER WHICH THE PC CHOOSED IT RANDOMLY")
    print("FOR EXAMPLE :")
    print("IF THE PC CHOOSED 60 AND YOU TELL 50 THE SYSTEM WILL SAY UP BUT IF YOU SAY 70 IT WILL SAY DOWN")
    print("IF YOU CHOOSE THE RIGHT NUMBER THEN YOU WILL WIN THE PARTY")
    print()

#making a function in french to print instructions for the game
def fr_udinstructions():
    print()
    print("INSTRUCTION DU JEU HAUT-BAS")
    print()
    print("TU DOIS TROUVER LE NOMBRE QUE LE PC A CHOISI AU HASARD")
    print("PAR EXEMPLE :")
    print("SI LE PC A CHOISI 60 ET TOI TU AS CHOISI 50 LE SYSTEME VA DIRE HAUT MAIS SI TU DIS 70 IL VA DIRE BAS")
    print("SI TU CHOISI LE BON NOMBRE ALORS TU VAS GAGNER LA PARTIE")
    print()

#making a function in english for the easy level
def UDEASY_EN():
    
    pc = random.randint(1,100) #we initialize the random number
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter '\"help\" for instructions")
        print("Enter a number to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        
        player = input("Enter your move : ")# asking the user to make a move
        
        if player.lower() == 'help': #if the user entered help we show him the instructions of the game
            clear()
            en_udinstructions()
            continue
        elif player.lower() == 'exit': #if it's exit we exit the game by breaking the code
            clear()
            break
        elif int(player) < pc : #if it's lower we say up
            print("UP")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc : #if it's higher we say down
            print("DOWN")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc : #if the number is found we end the game by breaking the code
            print(f"{name_en} FOUND THE NUMBER, CONGRATS!")
            time.sleep(2)
            clear()
            break
        else:
            print("WRONG INPUT") #if the input is not none of proposed then we ask again
            en_udinstructions()
            continue
   
#making a function in french for the easy level
def UDEASY_FR():
    pc = random.randint(1,100)
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Entre \"help\" pour les instructions")
        print("Entre un nombre pour jouer")
        print("Entre \"exit\" pour quitter")
        print("--------------------------------------")
        
        player = input("Entre ton choix : ")
        
        if player.lower() == 'help':
            clear()
            fr_udinstructions()
            continue
        elif player.lower() == 'exit':
            clear()
            break
        elif int(player) < pc :
            print("HAUT")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc :
            print("BAS")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc :
            print(f"{name_fr} A TROUVÉ LE NOMBRE, FELICITATIONS!")
            time.sleep(2)
            clear()
            break
        else:
            print("MAUVAIS INPUT")
            fr_udinstructions()
            continue

#making a function in english for the normal level
def UDNORMAL_EN():
    global name
    pc = random.randint(1,1000)
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter a number to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        
        player = input("Enter your mover : ")
        
        if player.lower() == 'help':
            clear()
            en_udinstructions()
            continue
        elif player.lower() == 'exit':
            clear()
            break
        elif int(player) < pc :
            print("UP")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc :
            print("DOWN")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc :
            print(f"{name_en} FOUND THE NUMBER, CONGRATS!")
            time.sleep(2)
            clear()
            break
        else:
            print("WRONG INPUT")
            en_udinstructions()
            continue           
  
#making a function in french for the normal level  
def UDNORMAL_FR():
    pc = random.randint(1,1000)
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Entre \"help\" pour les instructions")
        print("Entre un nombre pour jouer")
        print("Entre \"exit\" pour quitter")
        print("--------------------------------------")
        
        player = input("Entre ton choix : ")
        
        if player.lower() == 'help':
            clear()
            fr_udinstructions()
            continue
        elif player.lower() == 'exit':
            clear()
            break
        elif int(player) < pc :
            print("HAUT")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc :
            print("BAS")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc :
            print(f"{name_fr} A TROUVÉ LE NOMBRE, FELICITATIONS!")
            time.sleep(2)
            clear()
            break
        else:
            print("MAUVAIS INPUT")
            fr_udinstructions()
            continue  
    
#making a function in english for the hard level
def UDHARD_EN():
    pc = random.randint(1,10000)
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter a number to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
        
        player = input("Enter your mover : ")
        
        if player.lower() == 'help':
            clear()
            en_udinstructions()
            continue
        elif player.lower() == 'exit':
            clear()
            break
        elif int(player) < pc :
            print("UP")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc :
            print("DOWN")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc :
            print(f"{name_en} FOUND THE NUMBER, CONGRATS!")
            time.sleep(2)
            clear()
            break
        else:
            print("WRONG INPUT")
            en_udinstructions()
            continue

#making a function in french for the hard level
def UDHARD_FR():
    pc = random.randint(1,10000)
    
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Entre \"help\" pour les instructions")
        print("Entre un nombre pour jouer")
        print("Entre \"exit\" pour quitter")
        print("--------------------------------------")
        
        player = input("Entre ton choix : ")
        
        if player.lower() == 'help':
            clear()
            fr_udinstructions()
            continue
        elif player.lower() == 'exit':
            clear()
            break
        elif int(player) < pc :
            print("HAUT")
            time.sleep(1)
            clear()
            continue
        elif int(player) > pc :
            print("BAS")
            time.sleep(1)
            clear()
            continue
        elif int(player) == pc :
            print(f"{name_fr} A TROUVÉ LE NOMBRE, FELICITATIONS!")
            time.sleep(2)
            clear()
            break
        else:
            print("MAUVAIS INPUT")
            fr_udinstructions()
            continue   
       
#making sure that the code is running in this file
if __name__ == '__main__':
    
    #Asking the user to choose the language of the game
    print("1 POUR FRANCAIS")
    print("2 FOR ENGLISH")
    
    inp = int(input("1/2 : "))
    
    if inp == 1 :
        name_fr = input("Entre ton nom : ")#Asking user to enter his name
        while True:
            
            print()
            print("JOUONS !")
            print("CHOISI LE NIVEAU DU JEU")
            print("1 FACILE (1-100)")
            print("2 NORMAL (1-1000)")
            print("3 DIFFICILE (1-10000)")
            print("4 POUR QUITTER")
            print()
            
            try:
                choice = int(input("Entre ton choix : ")) #Asking the user to choose in which level does he want to play
            
            except ValueError: #if it's a valueError
                clear()
                print("Mauvais choix. Lis les instructions.") #You'll tell to the player it's a wrong choice
                continue #and making sure the code to not brak 
            
            if choice == 1:
                UDEASY_FR() #initialize the level easy
                
            elif choice == 2:
                UDNORMAL_FR() #initialize the level normal
            
            elif choice == 3:
                UDHARD_FR() #initialize the level hard
            
            elif choice == 4: #quitting the game
                break
            
            else: #if the number entered is not between 1 and 4
                clear()
                print("Mauvais Choix. Lis les instructions.")
          
    #the same for the english version      
    elif inp == 2 :
        name_en = input("Enter your name : ")
        while True:
            
            print()
            print("LET'S PLAY !")
            print("CHOOSE THE LEVEL OF THE GAME")
            print("1 EASY (1-100)")
            print("2 NORMAL (1-1000)")
            print("3 HARD (1-10000)")
            print("4 FOR EXIT")
            print()
            
            try:
                choice = int(input("Enter your choice : "))
            except ValueError:
                clear()
                print("Wrong Choice")
                continue
            
            if choice == 1:
                UDEASY_EN()
                
            elif choice == 2:
                UDNORMAL_EN()
            
            elif choice == 3:
                UDHARD_EN()
            
            elif choice == 4:
                break
            
            else:
                clear()
                print("Wrong choice. Read instructions.")
        
    
    
    