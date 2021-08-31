# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def position(L,value):
    k=0
    for i in L:
        for j in range(len(i)):
            if i[j]==value:
                posi=[k,j]
        k+=1
    return posi
def isKingsTour(board):
    for i in board:
        for j in range(len(i)):
            if i[j] not in range(1,len(board)**2+1):
                return False
    for i in range(1,len(board)**2):
        x=position(board,i)
        y=position(board,i+1)
        if abs(x[0]-y[0])==1 or abs(x[1]-y[1])==1:
            continue
        else:
            return False
    else:
        return True
    # Your code goes here...
    #pass
