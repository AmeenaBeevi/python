r="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
            r=r+"*"    
        else:      
            r=r+" "    
    r=r+"\n"    
print(r);