r="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or (row == 6 and column != 0 and column < 7)):  
            r=r+"*"    
        else:      
            r=r+" "    
    r=r+"\n"    
print(r);
