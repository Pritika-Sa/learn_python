import math
Friends = int(input("No.of.friends :"))
Shoes = int(input("No.of.shoes left :"))
Total_no_of_shoes = Friends * 2
Required_no_of_shoes = Total_no_of_shoes - Shoes
if(Required_no_of_shoes % 2==0):
    print(Required_no_of_shoes/2 , "pairs")
else:
    print(math.floor(Required_no_of_shoes/2) , "pairs and 1 shoe")