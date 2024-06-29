def menu_function():
    from main import user_choice_category, user_choice_dish

#מחלקת פרטי התפריט
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# מחלקת פסטה
class Pasta(MenuItem):
    def __init__(self, name, type, price):
        super().__init__(name, price)
        self.type = type


# מחלקת סלט
class Salad(MenuItem):
    def __init__(self, name, sauce, price):
        super().__init__(name, price)
        self.sauce = sauce


# מחלקת משקה
class Drink(MenuItem):
    def __init__(self, name, flavor, price):
        super().__init__(name, price)
        self.flavor = flavor

from Order import Order
#מחלקת תפריט
class Menu(Order):
    def __init__(self):
        self.Order = Order("", 0)
        self.menu_items = {
            "pasta": [
                Pasta(name="rose", type="With Rose", price=56),
                Pasta(name="mushroom Cream", type="Mushroom Cream", price=69)
            ],
            "salad": [
                Salad(name="dreamy salad", sauce="Garlic", price=59),
                Salad(name="caesar salad", sauce="Mustard", price=64)
            ],
            "drink": [
                Drink(name="orange Juice", flavor="Orange", price=14),
                Drink(name="coffee", flavor="Aromatic", price=17)
            ]
        }

    #הדפסת התפריט
    #Comprehentionשימוש ב
    def printMenu(self):
        menu_strings = [f"{category}\n" + "\n".join([f"  {item.name} - {item.price} NIS" for item in items]) for
                        category, items in self.menu_items.items()]
        print("\n\n".join(menu_strings))

    #בחירת מאיזה קטגוריה רוצים להזמין
    def chooseCategory(self, user_choice_category):
        if user_choice_category in self.menu_items:
            print(f"{user_choice_category} is a valid meal type.")

    #בחירת מאיזה מנה רוצים להזמין
    #generatorשימוש ב
    def chooseDish(self, user_choice_category, user_choice_dish):
            selected_item = next((item for item in self.menu_items[user_choice_category] if user_choice_dish == item.name),None)
            if selected_item:
                self.Order.myOrder.append(selected_item)
                print(f"{user_choice_dish} added to your order.")

    #הדפסה ללקוח את הפריט שבחר ועלותו ובסוף מסכם את סכום כל ההזמנה
    def printmy(self,myOrder):
       self.totalPayment=0
       for item in self.Order.myOrder:
           print(f"Your meal is: {item.name} and you need to pay: {item.price}")
           self.totalPayment += item.price
       print(f"{self.totalPayment} Amount to pay")

