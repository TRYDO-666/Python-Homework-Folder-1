import random

Rice = 45
Sugar = 40
Oil = 120
Rice_quantity = 3
Sugar_quantity = 2.5
Oil_quantity = 1.8 

Total_bill = (Rice * Rice_quantity) + (Sugar * Sugar_quantity) + (Oil * Oil_quantity)
print("Total bill is:", Total_bill) 

Bill_String = str(Total_bill)
print("Total bill in string format is:", Bill_String)

Bill_Integer = int(Total_bill)
print("Total bill in integer format is:", Bill_Integer)


Delivery_charge = random.randrange(5, 10)
print("Delivery charge is:", Delivery_charge)

Final_Bill = Total_bill + Delivery_charge
print("Final bill including delivery charge is:", Final_Bill)