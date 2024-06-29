from Order import Order
from Menu import Menu
def main_function():
    from Menu import Menu, Pasta, Salad, Drink
my_menu = Menu()
my_order = Order(Name=" ", customerPayment=0)

print("Welcome to your Restaurant\n")

#הדפסת התפריט
print("MENU:")
my_menu.printMenu()


while True:
    try:
        #הרצה של פונקציות ההזמנות ובדיקה תקינות
        user_choice_category = input("Choose the type of meal (type 'exit' to end): ")
        if user_choice_category.lower() == 'exit':
            break
        if user_choice_category not in my_menu.menu_items:
            raise ValueError("Invalid meal type. Please choose a valid category.")
        my_menu.chooseCategory(user_choice_category)

        user_choice_dish = input("\nEnter the name of the item you want to add to your order: ")
        if user_choice_dish not in [item.name for item in my_menu.menu_items[user_choice_category]]:
            raise ValueError("Invalid dish name. Please choose a valid dish.")
        my_menu.chooseDish(user_choice_category, user_choice_dish)

    except ValueError as ve:
        print(f"Error: {ve}")
    my_menu.printmy(my_order.myOrder)


#הרצת פונקציה תשלום ולקיחת פרטים מהלקוח
name = input("Enter your name")
customer_payment = int(input("Enter the payment amount entered into the cash register: "))
my_order = Order(Name=name, customerPayment=customer_payment)
my_order.processPayment(my_order.customerPayment, my_order.Name,my_menu.totalPayment)
print("the resit was printed")
