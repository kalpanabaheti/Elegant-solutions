#1 - 3rd Largest num in list - single iteration
'''
def large3():

    l = []
    for i in range(8):
        num = int(input("\nEnter number: "))
        l.append(num)

    m1 = l[0]
    m2 = l[1]
    m3 = l[2]
    
    for e in l:

        if e>m1:

            m3 = m2
            m2 = m1
            m1 = e
            
        elif e>m2:

            m3 = m2
            m2 = e

        elif e>m3:

            m3 = e
        
        else:
            
            pass



    print("\nRight! 3rd Largest Number is: ",m3)


#main environment


large3()

'''
#2 - Nth largest in list - single iteration
'''
def largen():

    
    l1 = []
    l2 = []

    for i in range(8):

        num = int(input("\nEnter: "))
        l1.append(num)

    l = l1
    l.sort()
    print(l,"\n")
    n = int(input("\nEnter n: "))
    
    if n>8:

        print("\nSorry, n cannot be greater than 8! Try again.\n")
        largen()

    k = n-1
    g = 0


    for i in range(n):

        l2.append(g)

    j = 0

    for e in l1: #Single iteration

        while e<l2[j]:

            j=j+1

        else:

            for i in range(k-1,j-1,-1):

                l2[i+1]=l2[i]
                
            l2[j]=e
            j = 0


                

    print("\nNth largest number through single iteration: ",l2[k])

largen()
'''

#3 - Pythogorean Triplet Check

'''
import math

def pythCheck():

    
    l1 = []
    l2 = []

    n = int(input("\nEnter number of elements: "))

    for i in range(n):

        num = int(input("\nEnter number: "))
        l1.append(num)

    l1.sort(reverse=True)

    flag = 0
    count = 0

    for i in range(n):

        for j in range(i+1,n):

            c = (l1[i]**2)-(l1[j]**2)
            sqrc = math.sqrt(c)
            sqr1 = int(math.ceil(sqrc))
            sqr2 = int(math.floor(sqrc))

            if sqr1==sqr2:

                for e in range(j+1,n):

                    if l1[e]==sqr1:

                        flag = 1
                        count+=1
                        print("\na,b,c can be ",sqr1,l1[j],l1[i])

                        

    if flag==0:

        print("\nNo Pythogorean Triplet here!")

    else:

        print("\nTotal count = ",count)
                        
                
pythCheck()
'''

#4 - Array of N packets with some number of sweets - M children (each get atleast 1 packet) - minimize maximum discrepency
'''
def minimize1():

    l1 = []

    n = int(input("\nEnter number of packets: "))
    for i in range(n):

        num = int(input("Enter number of sweets respectively (Must be a positive integer): "))
        l1.append(num)

    m = int(input("\nEnter number of children: "))

    ex = n-m

    l1.sort(reverse=True)

    l2 = l1[m:]
    l1 = l1[:m]
    print(l1)
    print(l2)

    for e in l2:

        l1[-1]+=e
        l2.remove(e)
        l1.sort(reverse=True)

    diff = l1[0]-l1[-1]
    print("\nMinimum difference between richest and poorest kid: ",diff)
        


minimize1()
'''

#5 - Variation of previous problem - each child gets exactly 1 packet - all packets need not be distributed.

'''
def minimize2():

    
    l1 = []

    n = int(input("\nEnter number of packets: "))
    for i in range(n):

        num = int(input("Enter number of sweets respectively (Must be a positive integer): "))
        l1.append(num)

    m = int(input("\nEnter number of children: "))
    l1.sort(reverse=True)
    print(l1)

    diff = l1[0]-l1[m-1]

    for i in range(1,n-m+1):

        d = l1[i]-l1[i+(m-1)]
        if d<diff:

            diff=d       

 
    print("\nMinimum difference: ",diff)


minimize2()
'''

#6 - First element where all LHS elements smaller and all RHS elements bigger
'''
def find():

    l1 = []

    n = int(input("\nEnter number of elements: "))
    for i in range(n):

        num = int(input("Enter number: "))
        l1.append(num)



    peak=l1[0]
    flag=0

    for i in range(n):

        if l1[i]>peak:

            peak=l1[i]
            flag=1

            for j in range(i+1,n):

                if l1[j]<peak:

                    flag=0

        if flag==1:

            break

    if flag==0:

        print("\nCondition not found in any case.")

    else:

        print("\nFirst case at position ",i," with value ",peak)


find()
'''

#7 - Matrix spiral traversal

'''

def spiral():

    l=[]

    m = int(input("\nEnter number of rows: "))
    n = int(input("\nEnter number of columns: "))

    for i in range(m):

        a=[]

        for j in range(n):

            num = int(input("\nEnter element: "))
            a.append(num)

        l.append(a)

    #display matrix

    for i in range(m):
        
        for j in range(n):

            print(l[i][j],end=' ')

        print("\n")


    count = 0
    stop = m*n

    i=0
    j=0

    r=m-1
    c=n-1
    flag=0

    while(count<stop):

        if i==c and j==c:

            print(l[i][j], end = ' ')
            count+=1

        for x in range(i,c):

            print(l[i][x],end = ' ')
            count+=1

        for x in range(i,r):

            print(l[x][c],end = ' ')
            count+=1

        for x in range(c,i,-1):

            print(l[r][x],end = ' ')
            count+=1

        for x in range(r,i,-1):

            print(l[x][j],end = ' ')
            count+=1

        i=i+1
        j=j+1
        r=r-1
        c=c-1



spiral()
        
'''
        
#8 - Equilibrium point (sum of preceding elements = sum of succeeding elements)

'''

def equilibrium():

    l1 = []

    n = int(input("\nEnter number of elements: "))
    for i in range(n):

        num = int(input("Enter number: "))
        l1.append(num)

    sum1 = 0
    sum2 = 0
    i = 1
    flag = 0
    pos = 0
    ele = 0
    fin = 0

    while(i<n-1):

        if i>n-i-1:
            flag = 1
            break

        for j in range(0,i):

            sum1 = sum1 + l1[j]

        j = i+1
        while(j<n and sum2<sum1):

            sum2 = sum2 +l1[j]
            j+=1

        else:

            if sum2==sum1 and j==n:

                flag = 0
                pos = i
                ele = l1[i]
                fin = sum1
                break


            else:

                sum1 = 0
                sum2 = 0
                flag = 1
                i+=1
                


    if flag==0:

        print("\nFirst equilibrium traversed is ",ele," at position ",pos+1," with sum: ",fin)

    else:

        print("\nNo equilibrium exists.")



equilibrium()

'''

#9 - From 1 to N all numbers are listed, except 1, find the number

'''

import random

def missing():

    l1 = []
    N = random.randint(5,50)
    num = random.randint(1,N)
    
    for i in range(1,N+1):

        if i!=num:
            l1.append(i)

    random.shuffle(l1)
    print(l1)

    s = 0
    m = l1[0]

    for e in l1:

        s = s + e

        if e>m:

            m=e

    total = int(m*(m+1)/2)

    if total==s:

        print("\nMissing number is: ",m+1)

    else:

        print("\nMissing number is: ",total-s)

    if m==N or m==N-1:

        print("\nVerified for N = ",N)

missing()
'''

#10 - Best time to buy and sell stocks
'''
def stock():

    l1 = []

    n = int(input("\nEnter number of days: "))
    for i in range(n):

        num = int(input("Enter respective stock value for the day: "))
        l1.append(num)

    j = 0
    l1.append(0)

    buy = l1[0]
    sell = l1[1]
    sellday = 2
    buyday = 1
    flag = 0

    for i in range(1,n+1):

        if l1[i]>=l1[i-1]:

            sell = l1[i]
            sellday = i+1

        else:

            if (buyday==sellday-1) and flag==0:
                buyday+=1
                sellday+=1
                continue

            print("\nBuy on day ",buyday," for ",buy)
            print("\nSell on day ",sellday," for ",sell)
            print("\nProfit: ",sell-buy)
            flag = 1

            buyday = i+1
            buy = l1[i]

    if flag==0:

        print("\nNo profit.")
           
stock()
'''
            

        

    

    

    


    

                

            




            
        
        

        

        

    

            
            
            
    

        

            















    
