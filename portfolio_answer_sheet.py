import sys

def question_answ():
    guess_count = 0
    guess_limit = 3 

    
    while guess_count < guess_limit: 
        guess_count += 1
        
        if input("Enter your guess: ") == "light yagami":
            print("You Got It!\n")
            break
        
        elif guess_count == 1:
            print("\nTry Again")
        
        elif guess_count == 2:
            print("\nhint: notebook\n")    
    
    else:
        guess_count = guess_limit
        print("\nMax attempts reached. Maybe next time...bye")
        sys.exit()  
            

def question2_answ():
    guess_count = 0
    guess_limit = 3
    
    while guess_count < guess_limit:
        guess_count += 1

        if input("Enter your guess: ") == "rock lee":
            print("You know your stuff!\n")
            break
        
        elif guess_count == 1:
            print("\nTry Again") 
        
        elif guess_count == 2:
            print("\nhint: taijutsu\n")   
    
    else:
        guess_count = guess_limit
        print("\nMax attempts reached. Maybe next time...bye") 
        sys.exit()   
            

def question3_answ():
    guess_count = 0
    guess_limit = 3
    
    while guess_count < guess_limit:
        guess_count += 1
    
        if input("Enter your guess: ") == "shoto todoroki":
            print("Nice Work!\n")
            break
        
        elif guess_count == 1:
            print("\nTry Again") 
        
        elif guess_count == 2: 
            print("\nhint: fire and ice\n")  
    
    else:
        guess_count = guess_limit
        print("\nMax attempts reached. Maybe next time...bye")
        sys.exit()    
            

def question4_answ():
     guess_count = 0
     guess_limit = 3
        
     while guess_count < guess_limit:
        guess_count += 1
    
        if input("Enter your guess: ") == "satoru gojo":
            print("Let's Go! One more to go!\n")
            break 
        
        elif guess_count == 1: 
            print("\nTry Again")
        
        elif guess_count == 2: 
            print("\nhint: blindfold\n")   
     
     else:
         guess_count = guess_limit
         print("\nMax attempts reached. Maybe next time...bye")
         sys.exit()    
            

def question5_answ():
    guess_count = 0
    guess_limit = 3
    
    while guess_count < guess_limit:
        guess_count += 1
    
        if input("Enter your guess: ") == "levi ackerman":
                print("Wow 5/5 is crazy!\n")
                break 
        
        elif guess_count == 1:
            print("\nTry Again")
        
        elif guess_count == 2: 
            print("\nhint: captain\n")  
    
    else:
        guess_count = guess_limit
        print("\nMax attempts reached. Maybe next time...bye")
        sys.exit()    
            
            


    


        
    
