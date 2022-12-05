def bill():
     prices = [5,10,15,20,25]
     total = 0
     week = 1     
     while week <= 7:         
         total = total + prices[0] + prices[1] + prices[2] + prices[3] + prices[4]         
         week = week + 1
         
     return total  
    
def main():      
    total = bill()     
    print("Total bill of chocolates: ", total)  
main()