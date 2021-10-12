import random


def run_game():
    # STEP 1. 
    '''
    The below code gives a random code
    that range between 1 and 8
    and checks if the code
    does not have any duplicate before breaking the loop.
    '''
    while True:
        comp = []
        for i in range(0, 4):
            n = random.randint(1,8)
            if n not in comp:
                comp.append(n)
        if len(comp) == 4:
            print('4-digit Code has been set. ' 
                  'Digits in range 1 to 8. '
                  'You have 12 turns to break it.')
            break    
    # STEP 2. 
    '''
    The below code get a codebreaker input
    checks if the code meet the required conditions
    and breaks the loop if meant.
    '''
    count = 12
    while True: 
        while True:
            try:
                user_code = []
                get_user = input(f'Input 4 digit code: ')
                for i in get_user:
                    # checks if the input range from 1 to 8
                    if int(i) in range(1,9): 
                        # append it if the top code checks are right 
                        user_code.append(int(i))   
                # if lenght is greater than 3 and less than 5, break the loop    
                if len(user_code) > 3 and len(user_code) < 5:       
                    break
                else:
                    print('Please enter exactly 4 digits.')  
            # if the is any error continue asking for input      
            except ValueError:                                  
                print('Please enter exactly 4 digits.') 
                continue
        # Step 3   
        '''
        The below code I created two copies of my original list
        and I used them for manipulating vaules that are inside
        ''' 
        correct = 0
        position = 0
        copy_comp = comp.copy()
        copy_guess = user_code.copy()
        for n in range(4):
            if copy_guess[n] == copy_comp[n]:   # if both index are the same          
                position += 1                   # add 1 to the position count
                copy_guess[n] = "removed"      # replace value with removed
                copy_comp[n] = "removed"       # replace value with removed
        for m in range(4):
            if copy_comp[m] in user_code:
                correct += 1
                copy_guess[copy_guess.index(copy_comp[m])] = "remove"
        print(f'Number of correct digits in correct place:     {position}')
        print(f'Number of correct digits not in correct place: {correct}')
        # Step 4
        '''
        The below code checks if turns are equal to 0
        and if codebreaker input is equal to codemaster.
        If one of those conditions is meant, it should break the 1st loop.
        '''
        if count == 0:
            break
        count -= 1
        if user_code == comp:
            print(f'Congratulations! You are a codebreaker!')
            print(f'The code was: {get_user}')
            break
        a = 'wrong. guess again.'
        b = 'Turns left: '
        print(f"{a.replace(a,b)}{count}")
        pass
    

if __name__ == "__main__":
    run_game()
