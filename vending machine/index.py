# customer Side Server
Req_name = input("Name of the requirement ")
No_of_req = int(input("enter the No of Product Required"))


# BAckend

# Product Available
Product_available = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5",
                     "Product 6", "Product 7", "Product 8", "Product 9", "Product 10", "Product 11"]                  
# check if item is available or not
Total_Product = len(Product_available)
index = 0
def check_availability():
    for i in range(0, Total_Product):
        
        if Req_name == Product_available[i]:
            print("Product is available")
            # remove the Product that has been fetched
            
            del Product_available[index]
            
            index = index + 1 

check_availability()             
            
# Display to user if Product available or not             
  
# show rest of the Products available
print(Product_available)

# User confirmation
User_confirmation = input("")

# this Project will be further improved as per the requirement 
