# rows = int(input())
# cols = int(input())

rows = 4
cols = 5

board = [[1]*cols for _ in range(rows)]

direction = 'bottom'
curRow=0
curCol=0
filled = 0
while True:        
  if curCol < 0 or curRow < 0 or curCol>=cols or curRow>=rows: break
  
  if (direction=='right') & (curCol < cols):
    if board[curRow][curCol] != 1: break
    
  if (direction=='top') & (curRow >= 0):
    if board[curRow][curCol] != 1: break
      
  if (direction=='left') & (curCol >= 0):
    if board[curRow][curCol] != 1: break
    
  if (direction=='bottom') & (curRow < rows):
    if board[curRow][curCol] != 1: break
    
  #BOTTOM
  if direction=='bottom':
    if curRow<rows:
      board[curRow][curCol] = 8
      filled+=1
      nextRow=curRow+1
      
      if nextRow==rows:
        direction='right'
        curCol+=1
        continue
      elif board[nextRow][curCol]==0:
        direction='right'
        curCol+=1
        continue
      else:
        if curCol<cols-1:
          board[curRow][curCol+1] = 0
        if curCol>0:
          board[curRow][curCol-1] = 0
        curRow=nextRow
        continue
    else:
      print('bottom', curRow, curCol)
      direction='right'
      curCol+=1
      continue
    
  # RIGHT
  if direction=='right':
    if curCol<cols:
      board[curRow][curCol] = 8
      filled+=1
      nextCol=curCol+1
      
      if nextCol==cols:
        direction='top'
        curRow-=1
        continue
      elif board[curRow][nextCol]==0:
        direction='top'
        curRow-=1
        continue
      else:
        if curRow<rows-1:
          board[curRow+1][curCol] = 0
        if curRow>0:
          board[curRow-1][curCol] = 0
        curCol=nextCol
        continue
    else:
      print('right', curRow, curCol)
      direction='top'
      curRow-=1
      continue
    
  #TOP
  if direction=='top':
    if curRow<rows:
      board[curRow][curCol] = 8
      filled+=1
      nextRow=curRow-1
      
      if nextRow<0:
        direction='left'
        curCol-=1
        continue
      elif board[nextRow][curCol]==0:
        direction='left'
        curCol-=1
        continue
      else:
        if curCol<cols-1:
          board[curRow][curCol+1] = 0
        if curCol>0:
          board[curRow][curCol-1] = 0
        curRow=nextRow
        continue
    else:
      print('top', curRow, curCol)
      direction='left'
      curCol-=1
      continue
    
  #LEFT
  if direction=='left':
    if curCol>=0:
      board[curRow][curCol] = 8
      filled+=1
      nextCol=curCol-1
      
      if nextCol<0:
        direction='bottom'
        curRow+=1
        continue
      elif board[curRow][nextCol]==0:
        direction='bottom'
        curRow+=1
        continue
      else:
        if curRow<rows-1:
          board[curRow+1][curCol] = 0
        if curRow>0:
          board[curRow-1][curCol] = 0
        curCol=nextCol
        continue
    else:
      print('left', curRow, curCol)
      direction='bottom'
      curRow+=1
      continue

for row in board:
  print(row)
print(filled)
