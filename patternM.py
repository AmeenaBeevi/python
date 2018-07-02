r="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):  
            r=r+"* "    
        else:      
            r=r+"  "    
    r=r+"\n"    
print(r);