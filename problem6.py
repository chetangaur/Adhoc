#! /usr/bin/python3

op=''' 
press 1 to view a single file
press 2 to view multiple file
press 3 to view operation similar to cat -n
press 4 to view operation similar to cat -e
'''
print(op)
a=int(input('Enter your choice'))
if a==1:
    i=input('Enter file name:')
    jj=open(i,"r")
    a=jj.read()
    print(a)
    #i.close()
elif a==2:
    i0=int(input("How many files do you want to show"))
    i1=[]
    print("write name of files ,whose content you want to know")
    for i in range(i0):
        
        i2=input()
        i1.append(i2)
    for i in i1:
        o1=open(str(i),'r')
        r1=o1.read()
    
        print(r1)
elif a==3:
    i=input("Enter your file name:") 
    f=open(i,'r')
    data=f.read()
    a=data.split('\n')
    l=1
    for i in a:
        print(str(l)+" "+i)
        l=l+1
elif a==4:
    i=input("Enter your file name:")
    f=open(i,'r')
    data=f.read()
    a=data.split('\n')
    l=1
    for i in a:
        print(i+'$')
        l=l+1
    
    
    
    

    
    
