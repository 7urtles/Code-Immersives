#//Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

#//A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

#//Ex:
#//Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
#//[[2,1,3],
#//[6,5,4],
#//[7,8,9]]
#//Output: 13 (1->5->7 or 1→4→8)

matrix = [
    [2,1,3],
    [6,5,4],
    [7,8,9]
]

x,y = 0,0
current = [x,y]


if x < len(matrix[0]):
    direction = input('\nDirection\n>')
    match direction:
        case 'up':
            y-=1
        case 'down':
            y+=1
        case 'left':
            x-=1
        case 'right': x+=1
    location = matrix[y][x]