menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
}
print("Welcome  to my dhaba")
print("pizza: RS40\npasta: RS50\nburger: RS60\nsalad: 70\ncoffee: 80\n")
order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item{item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not avaiable yet")
another_order= input("do you want to add another item/(yes/no)")
if another_order =="yes":
    item_2=input("Enter the name of second item=")
    if item_2 in menu:
     order_total += menu[item_2]
     print(f"item {item_2} has been added to order")
    else:
       print(f"orered item {item_2} is not avialable")
print(f"the total amount of item to pay is {order_total} ") 

