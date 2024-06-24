import random
a=1
b=99
com_Answer= random.randint(a,b)
print(com_Answer)
my_Answer=input('is it correct? \n c:CORRECT\n h:HIGHER \n l:LOWER \n')
while(my_Answer!='c'):
    if(my_Answer=='h'):
        a=com_Answer+1
        com_Answer=random.randint(a,b)
       
    elif(my_Answer=='l'):
        b=com_Answer-1
        com_Answer=random.randint(a,b)
    print(com_Answer)
    my_Answer=input('is it correct?')
print('I found it')
            


 