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
#8 - Combinations to reduce to 0
'''
def find_combinations(target, candidates):

    result = []

    def backtrack(start, target, combination):
    
        if target == 0:
            result.append(combination)
            return
        elif target < 0:
            return
        for i in range(start, len(candidates)):
            backtrack(i, target - candidates[i], combination + [candidates[i]])

    backtrack(0, target, [])
    return result

        
'''
        
#9 - Equilibrium point (sum of preceding elements = sum of succeeding elements)

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

#10 - From 1 to N all numbers are listed, except 1, find the number

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

#11 - Best time to buy and sell stocks
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
            
#12 - Minimum Platforms required for incoming and outgoing trains (waiting duration trains within a platform cannot overlap)

'''
def platformcount():

    arrive = []
    depart = []

    n = int(input("\nEnter number of trains arriving and departing in a day: "))

    for i in range(n):

        a = int(input("\nEnter arrival time of train (0000<HHMM<2359): "))
        d = int(input("\nEnter departure time of train (Arrival time<HHMM<2359): "))

        arrive.append(a)
        depart.append(d)

    l = []

    for i in range(n):

        train = []

        a = arrive[i]
        d = depart[i]

        train.append(a)
        train.append(d)

        l.append(train)

    #bubble sort l according to arrival times
    

    for i in range(n-1):
        for j in range(n-i-1):
            if l[j][0] > l[j+1][0] :
                l[j], l[j+1] = l[j+1], l[j]


    platform = []
    train = [l[0][0],l[0][1]]
    platform.append(train)
    last = l[0][1]
    system = []
    s = []
    s.append(platform)
    s.append(last)
    system.append(s)

    for i in range(1,n):

        flag = 0

        for j in range(len(system)):

            if l[i][0]>system[j][1]:

                system[j][1]=l[i][1]
                flag = 1
                trains = [l[i][0],l[i][1]]
                system[j][0].append(trains)
                break

        if flag==0:

            newlast = l[i][1]
            train = [l[i][0],l[i][1]]
            trains = [] 
            trains.append(train)
            newplat = []
            newplat.append(trains)
            newplat.append(newlast)
            system.append(newplat)

    for k in range(len(system)):

        print("\nPlatform: ",k+1)
        plat = system[k][0]

        for j in range(len(plat)):

            train = plat[j]

            print("\nTrain ",j+1,": ",train[0]," : ",train[1])

    print("\nNumber of platforms required: ",len(system))
                  

platformcount()
'''

#13 - Merge two sorted arrays into single sorted array - do not use extra space - time complexity O((n+m)log(n+m))  
'''
import time
def merge():

    l1 = []
    l2 = []

    n = int(input("\nEnter number of elements in first array: "))
    for i in range(n):

        num = int(input("Enter element: "))
        l1.append(num)

    m = int(input("\nEnter number of elements in second array: "))
    for i in range(m):

        num = int(input("Enter element: "))
        l2.append(num)

    l1.sort()
    print(l1)
    l2.sort()
    print(l2)

    lm = []
    i=0
    j=0

    s = time.time()

    while((i<n) and (j<m)):

        if l1[i]<=l2[j]:

            lm.append(l1[i])
            i+=1
            
        else:

            lm.append(l2[j])
            j+=1        

    else:

        f = time.time()

        if i!=n:

            for k in range(i,n):

                lm.append(l1[k])

        else:

            for k in range(j,m):

                lm.append(l2[k])

    print("\nMerged and sorted list: ",lm)
    print("\nTime taken in seconds: ",f-s)


merge()
'''
        
#14 - Find size of minimum subset that gives maximum binary result on OR operation

'''
def orSubset():

    size = int(input("\nEnter number of elements: "))
    arr = []
    for i in range(size):
        el = int(input("\nEnter element: "))
        arr.append(el)
    arr.sort(reverse=True)

    binarr = []
    for el in arr:
        binstr = bin(el).replace("0b","")
        binarr.append(binstr)
    print(binarr)

    index = len(binarr[0])
    #print(index)
    pos = 1
    update = '0'*index
    #print(update)
    count = 999
    finarr = []

    for i in range(index):

        flag1 = 0

        for j in range(len(update)):
            if update[j] == '0':
                count = len(update)-j
                #print(j)
                break

        upperlim = 2**(count+1)
        lowerlim = 2**count
        maxel = 0

        if update!=('1'*index):
        
            for el in binarr:

                value = 0
                power = len(el)
                pos = power - count
                flag2 = 0
                for j in range(len(el)):
                    if el[j] == '1':
                        value = value + (2**power)
                        #print(value)
                        if j == pos:
                            flag2 = 1
                    power = power - 1

                if (value > maxel) and (value >= lowerlim) and (flag2 == 1):

                    maxel = value
                    ins = el
                    flag1 = 1

            #print("flag: ",flag1)
            if flag1 == 1:

                binarr.remove(ins)
                #print(binarr)

                x = len(update)-len(ins)
                y = 0
                new = ''
                for i in range(len(update)):

                    if i>=x:

                        temp1 = int(update[i])
                        temp2 = int(ins[y])
                        replace = str(temp1 or temp2)
                        new = new+replace
                        y = y + 1

                    else:

                        new = new+update[i]

                update = new
                        
                #print(int(update,2))
                finarr.append(int(ins,2))
                #print(finarr)

        else:

            break

    print(int(update,2))
    print(finarr)

#main environment

orSubset()
'''

#15 - Number of ways of splitting a given string into 2 so that each substring has the same number of unique characters - optimized version
'''
def splitString():

    string = input("Enter string: ")
    count = 0
    unique = []
    diff = 0
    flag = 0
    n = 1

    for i in range(len(string)-1):
        if string[i]!=string[i+1]:
            flag = 1
            break

    if flag == 0:
        count = len(string) - 1
        print("\nCount: ",count)

    else:

        while n!=(len(string)-1):

            sub1 = string[:n]
            sub2 = string[n:]

            for i in sub1:
                if i not in unique:
                    unique.append(i)
            count1 = len(unique)
            unique = []

            for i in sub2:
                if i not in unique:
                    unique.append(i)
            count2 = len(unique)
            unique = []

            diff = abs(count2 - count1)
            if diff == 0:
                count = count + 1

            if diff>2:

                jump = diff//2
                n = n+jump
    

            else:

                n = n+1

        print("\nCount: ",count)
                

#main environment

splitString()

'''

#16 - Finding minimum domino rotations for an equal row.

'''

def equalRows():

    A = []
    B = []
    i = 0

    while True:

        n = int(input("\nEnter the length of rows (between 2 and 20000): "))
        if 2<=n<=20000:
            break
        else:
            print("\nPlease follow instructions.")
            continue

    while i<n:
        
        try: 
            up,down = [int(x) for x in input().split()]
            if 0<up<7 and 0<down<7:
                A.append(up)
                B.append(down)
                i = i+1
            else:
                print("Value out of range, try again.")
                
        except:
            print("Value out of range, try again.")


    count = [0,0]
    a = A[0]
    b = B[0]

    for i in range(n):
        
        if A[i] == a:
            pass
        elif B[i] == a:
            count[0] = count[0] + 1
        else:
            count[0]=n
            break
          
            

    for i in range(n):
        if B[i] == b:
            pass
        elif A[i] == b:
            count[1] = count[1] + 1
        else:
            count[1]=n
            break


    if count == [n,n]:
        return -1
    
    else:
        return min(count)
            

#main environment

y = equalRows()

print("\nMinimum Rotations: ",y)
                      
'''

#17 - Two people watering plants simultaneously from two ends, refilling needed if plant demand is more than water can supply, find the number of total refills of both people together.

'''
def waterPlant():

    cap1 = int(input("\nEnter capacity of first watering can: "))
    cap2 = int(input("\nEnter capacity of second watering can: "))

    limit = min(cap1,cap2)
    print("\nNote that plant needs cannot exceed ",limit," units of water.")
    arr = []
    i = 0
    n = int(input("\nEnter number of plants: "))

    while i<n:

        need = int(input("\nEnter the amount of water the plant needs: "))

        if need>limit:
            print("\nPlease do not exceed the water limit.")
    
        else:
            arr.append(need)
            i = i+1

    mid = 0
    count = 2 #They refill each once at the beginning
    remwater1 = cap1
    remwater2 = cap2

    if n%2 == 0:

        sub1 = arr[:(n//2)]
        sub2 = arr[(n//2):]
        sub2 = sub2[::-1]

    else:

        sub1 = arr[:(n//2)]
        print(sub1)
        mid = n//2
        print(mid)
        sub2 = arr[(mid+1):]
        sub2 = sub2[::-1]
        print(sub2)

    for i in sub1:

        if i <= remwater1:
            remwater1 = remwater1 - i

        else:
            remwater1 = cap1 - i
            count = count + 1

    for i in sub2:

        if i <= remwater2:
            remwater2 = remwater2 - i

        else:
            remwater2 = cap2 - i
            count = count + 1

    if mid == 0:

        return count

    else:

        if arr[mid] > (remwater1 + remwater2):

            count = count + 1
            return count

        else:

            return count

#main environment

y = waterPlant()
print("Number of total refills: ",y)
'''

#18 - M people vote for their favorite fruits among N fruits (each person has their order of preference), the least popular fruit is removed till only one fruit is returned.

'''
def favFruit():


    n,m = [int(x) for x in input().split()]

    arrprefer = []

    for i in range(m):

        peepsarr = list(map(int, input().split()))
        arrprefer.append(peepsarr)

    fruits = [int(x) for x in range(1,n+1)]
    score = []
    count = 0

    while len(fruits)!=1:
        
        for el in fruits:
            for person in arrprefer:
                if el == person[0]:
                    count = count + 1
            score.append(count)
            count = 0

        minval = min(score)
        for i in range(len(score)):
            
            if score[i]==minval:
                
                z = fruits.pop(i)
                
                for person in arrprefer:
                    try:
                        person.remove(z)
                    except:
                        pass
    
                break

        score = []
        
                    
    else:

        return fruits[0]
            

#main environment

s = favFruit()
print("\nFav Fruit: ",s)
'''

#19 - Given a sequence of digits (1-9), check if they can be rearranged into a number divisible by 11.
#Need to work on time constraint - refer elevenagram on KickStart
'''
from itertools import combinations
def divisibleby11():

    n = int(input("\nEnter number: "))
    nstr = str(n)
    arr = [int(x) for x in nstr]
    if len(arr) == 1:
        if arr[0] == 0:
            return 1
        else:
            return -1
        
    k = len(arr)//2
    b = arr[:] 

    comblist = combinations(arr,k)
    flag = 0

    for a in comblist:

        a = list(a)

        sum1 = 0
        sum2 = 0

        for i in range(len(a)):
            b.remove(a[i])
            sum1 = sum1 + a[i]
        print(sum1)
        print(b)

        for j in b:
            sum2 = sum2 + j
        print(sum2)
        b = arr[:]

        diff = abs(sum1 - sum2)

        if diff%11 == 0:
            flag = 1
            break

    if flag == 0:

        print("\nNo combination possible.")

    else:

        print("\nCombination possible!")

#main environment

y = divisibleby11()
if y == -1:    
    print("\nNo combination possible.")
if y == 1:
    print("\nCombination possible.")

'''

        

        

        
            

    

    

            

        

















    
    
