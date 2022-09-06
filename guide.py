import random as rm

class Address ():
    
        def cl_kr(choose): #generates the number of the street

            
            firstPart = []

            '''
            The base of the logic its that first we call cl_kr(0) to can take the first part of the address
            second we take the 1 element in firstPart wich say if the first part of the addres its a cl or a Kr using pick
            taking in count the 1 element we call cl_kr() with it and that return the rest a cl or a kr depending of wich was choose before
            '''

            def pick(): #choose if the first part of the address will be a cl or a kr 
                firstPart.append(cl()if rm.randint(1,2) == 1 else kr()) 
                # firstPart.append(0)
                # return(firstPart)   

            def cl(): # returns the number of the cl
                firstPart.append(rm.randint(0,170))
                firstPart.append(1)
                # print(cl_str, '3')
                # return(firstPart)
                
            def kr():# returns the number of the kr
                firstPart.append(rm.randint(0,120))
                firstPart.append(2)
                # print(kr_str),'3' 
                # return(firstPart)

            if choose == 0:
                pick() 
            if choose == 1:
                kr()    
            if choose == 2:
                cl()
            return(firstPart)
            
        
        def cardinal():#generates south or north
            direcction = ['sur','norte']
            return(direcction[rm.randrange(0,1)])
        
        def nomen (dire):
            if dire == 1:
                return('Cl')
            if dire == 2:
                return('Kr')