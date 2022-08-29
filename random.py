import random as rm
from secrets import choice 
class Address ():
    #principal method wichi generate the address
    def address_generator ():
        address = '' 

        def cl_Kr(): #generates the number of the street
            return(rm.randint(0,170)if rm.randint(1,2) == 1 else rm.randint(1,120))
        
        def cardinal():#generates south or north
            return(rm.choice('sur','norte'))
        

            
