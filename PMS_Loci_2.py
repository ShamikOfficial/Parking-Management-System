import pandas as pd

def position():
    #Matrix of parking lot
    #T=Taken
    #S=Start
    #E=Empty
    #P=Path
    #Sample format
    '''temp=[
    ['S','P','P','P','E'],
    ['P','T','T','P','E'],
    ['P','E','E','P','E'],
    ['P','T','T','P','E'],
    ['P','P','P','P','E'],
    ['E','E','E','E','E']
    ]'''
    #pd.DataFrame(temp).to_csv("map4.csv")
    ma=[] #empty temporary matrix
    df = pd.read_csv("map4.csv",usecols=range(1,11)) #import matrix map from csv file
    temp = df.to_numpy().tolist()
    #print(temp)
    ma=temp
    n1=11 #horizontal rows
    n2=10 #vertical column


    for x in range(n1):
        for y in range(n2):
            if ma[x][y] == 'S': #begin at Start
                beg = [0, x, y]

    stack = [] #Empty stack for storing distance
    stack.append(beg)
    count = 0
    while True :
        p = stack[count]
        count += 1
        x = p[1]
        y = p[2]

        #condition for finding closet empty slot
        if x-1>=0 and ma[x-1][y]=='E':
            return(p[0]+1,x-1,y) #return distance,x value,y value
            #temp[x-1][y]='T'
            #print(temp,ma)
            exit()
        if x+1<n1 and ma[x+1][y]=='E':
            return(p[0]+1,x+1,y)#return distance,x value,y value
            #temp[x+1][y]='T'
            #print(temp,ma)
            exit()
        if y-1>=0 and ma[x][y-1]=='E':
            #temp[x][y-1]='T'
            return(p[0]+1,x,y-1)#return distance,x value,y value
            #print(temp,ma)
            exit()
        if y+1<n2 and ma[x][y+1]=='E':
            #temp[x][y+1]='T'
            return(p[0]+1,x,y+1)#return distance,x value,y value
            #print(temp,ma)
            exit()
        #
        if x-1>=0 and ma[x-1][y]=='P':
            stack.append([p[0]+1, x-1, y])
            ma[x-1][y] = p[0]+1
        if x+1<n1 and ma[x+1][y]=='P':
            stack.append([p[0]+1, x+1, y])
            ma[x+1][y] = p[0]+1
        if y-1>=0 and ma[x][y-1]=='P':
            stack.append([p[0]+1, x, y-1])
            ma[x][y-1] = p[0]+1
        if y+1<n2 and ma[x][y+1]=='P':
            stack.append([p[0]+1, x, y+1])
            ma[x][y+1] = p[0]+1

#s,a,b=position()

#print(a,b)

#pd.DataFrame(temp).to_csv("map6.csv")
