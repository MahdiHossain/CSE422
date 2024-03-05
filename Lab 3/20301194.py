import random 

stid = input('Enter your student ID: ')

stud = ''

for i in stid:
    if i == '0':
        stud += '8'
    else:
        stud += i

mini = int(stud[4])
win = int(stid[-1] + stid[-2])
maxi = int(win * 1.5)

rlist = [random.randint(mini, maxi) for x in range(8)]

def alpha_beta(position, depth, optimus, alpha, beta, val):
    if depth == 0:
        return val[position]

    if optimus:
        imax = float('-inf')

        for i in range(2):
            i += position * 2 
            nval = alpha_beta(i, depth - 1 , False, alpha, beta, val)
            imax = max(imax, nval)
            alpha = max(imax, alpha)
            if alpha >= beta:
                break
        return imax
    
    else:
        imin = float('inf')
        for i in range(2):
            i += position * 2 
            nval = alpha_beta(i, depth - 1, True, alpha, beta, val)
            imin = min(imin, nval)
            beta = min(imin, beta)
            if  alpha >= beta:
                break
        return imin

wpoints = alpha_beta(0, 3, True, float('-inf'), float('inf'), rlist)

print('Generated 8 random points between the minimum and maximum point limits: ', rlist)
print('Total points to win: ', win)
print('Achieved point by applying alpha-beta pruning = ', wpoints)

if wpoints >= win:
    print('The winner is Optimus Prime')
else:
    print('The winner is Megatron')

j = 0
shuffle = []
winc = 0
wlist = []

while j < int(stud[3]):
    shuffle = random.sample(rlist, len(rlist))
    winres = alpha_beta(0, 3, True, float('-inf'), float('inf'), shuffle)
    wlist.append(winres)
    if winres >= win:
        winc += 1
    j += 1

print('\nAfter the shuffle: ')
print('List of all points values from each shuffles: ', wlist)
print('The maximum value of all shuffles:', max(wlist))
print(f'Won {winc} times out of {stud[3]} number of shuffles')