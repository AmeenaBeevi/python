r="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            r=r+"*"    
        else:      
            r=r+" "    
    r=r+"\n"    
print(r);