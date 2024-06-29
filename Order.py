#הוספת ספריה של תאריך
from datetime import datetime
# בניית תאריך בפורמט מסוים
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


#מחלקת הזמנה
class Order:
    def __init__(self, Name, customerPayment):
        self.Name = Name
        self.myOrder = []
        self.customerPayment = customerPayment
        self.totalPayment = 0

    #תשלום והדפסת קבלה
    def processPayment(self, customerPayment, Name,totalPayment):
        with open('OrderInvoice.txt', 'w') as file:
            file.write(f"{Name}, your order was placed on {current_date}\n")
            file.write(f"Total amount to pay: {totalPayment} $")
            file.close()
        if customerPayment < totalPayment:
            print(f"You need to add: {totalPayment - customerPayment} $")
        elif customerPayment > totalPayment:
            print(f"You are entitled to: {customerPayment - totalPayment} $")
        else:
            print("Payment is complete.")