#Enjoy the game
Grid=[
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
      ['⚪','⚪','⚪','⚪','⚪','⚪','⚪'],
    ]
print('Enjoy! Note: If like to quit game, type Yes')
Blue=0
Green=0
while True:
  WonGame=0
  LabelThing=0
  Quit=input('Like to quit(Yes/No)?: ')
  if Quit=='Yes':
    print('End game')
    break
  Columns=int(input('How many columns?: '))
  Rows=int(input('How many rows?: '))
  Label=[]
  Grid=[]
  h=0
  i=0
  while WonGame!='Yes':
    for p in range(Columns):
      Emoji='\U00000030'
      Emoji=int(Emoji)+p
      Label.append(Emoji)
    for k in Label:
      print(k,end='\t')
    print()
    for q in range(Rows):
      Grid.append([])
    while h<Rows:
      for r in range(Columns):
        while i<Columns:
          Grid[h].append('⚪')
          i=i+1
      h=h+1
      i=0
    for lists in Grid:
      for i in lists:
        print(i,end='\t')
      print()
    while WonGame!='Yes':
      x=0
      y=1
      for c in range(Rows):
        d=Grid[c].count('⚪')
      if d==0:
        print('Draw!')
        print('blue:',Blue)
        print('green:',Green)
        WonGame='Yes'
      if x%2==0 and WonGame!='Yes':
        x=x+1
        y=y+1
        print('🔵 Turn!')
        z=int(input('Which column?: '))
        while z<0 or z>=Columns:
          z=int(input('No such column. Which column?: '))
        else:
          h=Rows-1
          while h>=0:
            if Grid[h][z]=='⚪':
              Grid[h].pop(z)          
              Grid[h].insert(z,'🔵')
              break
            else:
              h=h-1
        for k in Label:
          print(k,end='\t')
        print()
        for lists in Grid:
          for i in lists:
            print(i,end='\t')
          print()
        for m in range(len(Grid[0])):
          for b in range(len(Grid)):
            if b>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b-1][m]==Grid[b-2][m]==Grid[b-3][m]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if m>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b][m-1]==Grid[b][m-2]==Grid[b][m-3]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b>=3 and m>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b-1][m-1]==Grid[b-2][m-2]==Grid[b-3][m-3]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b>=3 and m<len(Grid[0])-3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b-1][m+1]==Grid[b-2][m+2]==Grid[b-3][m+3]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b<len(Grid)-3 and m>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b+1][m-1]==Grid[b+2][m-2]==Grid[b+3][m-3]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b<len(Grid)-3 and m<len(Grid[0])-3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🔵'==Grid[b][m]==Grid[b+1][m+1]==Grid[b+2][m+2]==Grid[b+3][m+3]:
                print('🔵 Won!')
                Blue=Blue+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes' 
      if y%2==0 and WonGame!='Yes':
        x=x+1
        y=y+1
        print('🟢 Turn!')
        l=int(input('Which column?: '))
        while l<0 or l>=Columns:
          l=int(input('No such column. Which column?: '))
        else:
          h=Rows-1
          while h>=0:
            if Grid[h][l]=='⚪':
              Grid[h].pop(l)          
              Grid[h].insert(l,'🟢')
              break
            else:
              h=h-1
        for k in Label:
          print(k,end='\t')
        print()
        for lists in Grid:
          for i in lists:
            print(i,end='\t')
          print()
        for m in range(len(Grid[0])):
          for b in range(len(Grid)):
            if b>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b-1][m]==Grid[b-2][m]==Grid[b-3][m]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if m>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b][m-1]==Grid[b][m-2]==Grid[b][m-3]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b>=3 and m>=3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b-1][m-1]==Grid[b-2][m-2]==Grid[b-3][m-3]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b>=3 and m<len(Grid[0])-3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b-1][m+1]==Grid[b-2][m+2]==Grid[b-3][m+3]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b<len(Grid)-3 and m>len(Grid[0])-3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b+1][m-1]==Grid[b+2][m-2]==Grid[b+3][m-3]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
            if b<len(Grid)-3 and m<len(Grid[0])-3 and Rows>=4 and Columns>=4 and WonGame!='Yes':
              if '🟢'==Grid[b][m]==Grid[b+1][m+1]==Grid[b+2][m+2]==Grid[b+3][m+3]:
                print('🟢 Won!')
                Green=Green+1
                print('blue:',Blue)
                print('green:',Green)
                WonGame='Yes'
