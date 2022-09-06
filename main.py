from guide import Address 
        

if __name__ == '__main__':
    first = [] 
    first = Address.cl_kr(0) # calls the cl_kr to can catch te first part of the address
    
    second_opc = Address.cl_kr(first[1]) # calls the cl_kr to can catch te second part of the address using the number wich ist returned with the first part of the address
    
    third_opc = Address.cardinal() # calls cardinal to know if the first part will be in the south or the north

    firsOfAll = Address.nomen(first[1]) # calls nomen to can show if the first part of the address if a cl or a Kr 

    print(f'{firsOfAll} {first[0]} {third_opc} # {second_opc[0]}') # concatenate all the data
    # print(second_opc)

    # print(second,'2')
    # print(second_opc, '2')


        

            
