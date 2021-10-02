#importing the time module
import time 

#welcoming the user
name = raw_input("What is your name? ") 

print "Hello, " + name, "Time to play hangman!" 

print "
" 

#wait for 1 second
time.sleep(1) 

print "Start guessing..."
time.sleep(0.5) 


word = "secret" 

#creates a variable with an empty value
guesses = '' 

#determine the number of turns
turns = 10 

# Create a while loop 

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero 

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break              

    

   
    guess = raw_input("guess a character:") 

   
    guesses += guess                    

   
    if guess not in word:  

     
        turns -= 1        

    
        print ("Wrong")    

    
        print ("You have", + turns, 'more guesse') 

    
        if turns == 0:           
    
        
            print ("You Lose")
