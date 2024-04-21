import mysql.connector
from datetime import datetime
from mysql.connector import Error

conn = mysql.connector.connect(
    host="127.0.0.1",  # ip address
    user="root",  # username
    password="root", #password
    database="ORG" #database name
)
cursor = conn.cursor()



def fetch_admin_notifications(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Admin_Notifications")
    notifications = cursor.fetchall()
    cursor.close()
    if notifications:
        print("Low stock notifications:")
        for notification in notifications:
            print(notification)
    else:
        print("No notifications found.")
def admin_sign_in(conn):
    cursor = conn.cursor()
    while True:
        Username = input("Enter your username: ")
        Password = input("Enter your password: ")
        cursor.execute("SELECT * FROM Admin WHERE Username = %s AND Password = %s", (Username, Password))
        admin = cursor.fetchone()
        if admin:
            print("Admin Sign-in successful!")
            return admin[0]
        else:
            print("Invalid username or password. Please try again.")
            return None
    cursor.close()
def sign_in(conn):
    cursor = conn.cursor()
    while True:
        Username = input("Enter your username: ")
        Password = input("Enter your password: ")
        cursor.execute("SELECT * FROM Users WHERE Customer_ID = %s AND Password = %s", (Username, Password))
        user = cursor.fetchone()
        if user:
            print("Sign-in successful!")
            return 1, Username
            break
        else:
            print("Invalid username or password. Please try again.")
            return 0, None
            break
    cursor.close()
def sign_up(conn):
    cursor = conn.cursor()
    while True:
        username = input("Enter your username: ")
        cursor.execute("SELECT * FROM Users WHERE Customer_ID = %s", (username,))
        if cursor.fetchone():
            print("Username already exists. Please choose a different one.")
            continue
        password = input("Enter your password: ")
        name_first = input("Enter your first name: ")
        name_last = input("Enter your last name: ")
        contact_number = input("Enter your contact number: ")
        house_no = input("Enter your house number: ")
        email_id = input("Enter your Email ID: ")
        street_no = input("Enter your street number: ")
        zipcode = input("Enter your zipcode: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        age = input("Enter your age: ")
        coupons_availability = input("Enter your coupons availability (0 for False, 1 for True): ")
        cursor.execute("INSERT INTO Users (Customer_ID, password, Name_First_Name, Name_Last_Name, Contact_number, House_No, Street_no, Zipcode, Date_of_Birth, Email_ID, Age, Coupons_Availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (username, password, name_first, name_last, contact_number, house_no, street_no, zipcode, dob, email_id, age, coupons_availability))
        conn.commit()
        print("Sign-up successful!")
        break
    cursor.close()

def vendor_signin(conn):
    cursor = conn.cursor()
    while True:
        Vendor_Username = input("Enter your vendor username: ")
        Vendor_Password = input("Enter your vendor password: ")
        cursor.execute("SELECT * FROM Vendor WHERE Vendor_Username = %s AND Vendor_Password = %s", (Vendor_Username, Vendor_Password))
        vendor = cursor.fetchone()
        if vendor:
            print("Vendor Sign-in successful!")
            cursor.close()
            return vendor[0]
        else:
            print("Invalid username or password. Please try again.")
            cursor.close()
            return None
    

def vendor_signup(conn):
    cursor = conn.cursor()
    while True:
        Vendor_Username = input("Enter your vendor username: ")
        cursor.execute("SELECT * FROM Vendor WHERE Vendor_Username = %s", (Vendor_Username,))
        if cursor.fetchone():
            print("Username already exists. Please choose a different one.")
            continue
        Vendor_Password = input("Enter your vendor password: ")
        Contact_number = input("Enter your contact number: ")
        Warehouse_no = input("Enter your warehouse number: ")
        Street_no = input("Enter your street number: ")
        Zipcode = input("Enter your zipcode: ")
        Email_ID = input("Enter your Email ID: ")
        cursor.execute("INSERT INTO Vendor (Vendor_Username, Vendor_Password, Contact_number, Warehouse_no, Street_no, Zipcode, Email_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (Vendor_Username, Vendor_Password, Contact_number, Warehouse_no, Street_no, Zipcode, Email_ID))
        conn.commit()
        print("Vendor Sign-up successful!")
        break
    cursor.close()

def delivery_executive_signin(conn):
    cursor = conn.cursor()
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")
    cursor.execute("SELECT * FROM Delivery_Executive WHERE Username = %s AND Password = %s", (Username, Password))
    executive = cursor.fetchone()
    if executive:
        print("Delivery Executive Sign-in successful!")
        cursor.close()
        return executive[0]
    else:
        print("Invalid username or password. Please try again.")
        cursor.close()
        return None



def delivery_executive_signup(conn):
    cursor = conn.cursor()
    while True:
        username = input("Enter your username: ")
        cursor.execute("SELECT * FROM Delivery_Executive WHERE username = %s", (username,))
        if cursor.fetchone():
            print("username already exists. Please choose a different one.")
            continue
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_id = input("Enter your email ID: ")
        contact_number = input("Enter your contact number: ")
        house_no = input("Enter your house number: ")
        street_no = input("Enter your street number: ")
        zipcode = input("Enter your zipcode: ")
        city = input("Enter your city: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        cursor.execute("INSERT INTO Delivery_Executive (First_Name, Last_Name, Email_ID, Contact_number, House_No, Street_no, Zipcode, City, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, email_id, contact_number, house_no, street_no, zipcode, city, username, password))
        conn.commit()
        print("Executive sign-up successful!")
        break
    cursor.close()

def find_available_executive():
    sql_count_orders = "SELECT Executive_ID, COUNT(*) AS order_count FROM Delivers GROUP BY Executive_ID"
    cursor.execute(sql_count_orders)
    executive_orders = cursor.fetchall()
    
    available_executives = [executive[0] for executive in executive_orders if executive[1] < 3]
    
    return available_executives

def assign_order_to_executive(Executive_ID, Order_ID, customer_id, quantity, total_transaction_amount):
    sql_insert_order_details = "INSERT INTO ORDER_DETAILS (Executive_ID, Customer_ID, Order_ID, Quantity, Total_Transaction_Amount) VALUES (%s, %s, %s, %s, %s)"
    val_order_details = (Executive_ID, customer_id,  Order_ID, quantity, total_transaction_amount)
    cursor.execute(sql_insert_order_details, val_order_details)
    conn.commit()
    
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    sql_insert_delivers = "INSERT INTO Delivers (Executive_ID, Customer_ID, Order_ID, Date_of_delivery, Time_of_delivery, Delivery_Status) VALUES (%s, %s, %s, %s, %s, %s)"
    val_delivers = (Executive_ID, customer_id, Order_ID, current_date, current_time, 0)
    cursor.execute(sql_insert_delivers, val_delivers)
    conn.commit()
    print(f"Order {Order_ID} assigned to Executive {Executive_ID} successfully.")

cursor.execute("CREATE TRIGGER IF NOT EXISTS notify_low_quantity\
    AFTER UPDATE ON Product\
    FOR EACH ROW\
    BEGIN\
        IF NEW.Quantity < 10 THEN\
            INSERT INTO Admin_Notifications (Message, Notification_Date)\
            VALUES (CONCAT('Product ', NEW.Product_ID, ' is running low in quantity. Please restock.'), CURDATE());\
        END IF;\
    END;")

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS update_product_after_purchase AFTER INSERT ON Purchases_from
    FOR EACH ROW
    BEGIN
        IF NOT EXISTS (
            SELECT 1 FROM PRODUCT AS p
            INNER JOIN vendor_inventory AS i ON p.Name = i.Book_Name AND p.Vendor_ID = i.Vendor_ID
            WHERE i.vendor_inventory_id = NEW.vendor_inventory_id
        ) THEN
            INSERT INTO Product (Name, Price, Quantity, Vendor_ID, Username, Genre, ratings)
            SELECT v.Book_Name, v.Price + 10, p.Quantity, v.Vendor_ID, p.Username, v.Genre, v.ratings
            FROM Purchases_from AS p
            INNER JOIN vendor_inventory AS v ON p.vendor_inventory_id = v.vendor_inventory_id
            WHERE p.vendor_inventory_id = NEW.vendor_inventory_id;
        ELSE
            UPDATE Product AS p
            INNER JOIN vendor_inventory AS i ON p.Name = i.Book_Name AND p.Vendor_ID = i.Vendor_ID
            SET p.Quantity = p.Quantity + NEW.Quantity
            WHERE p.Name = i.Book_Name AND p.Vendor_ID = i.Vendor_ID;
        END IF;
    END
""")

def acquire_lock(lock_type, table_name):
    """
    Acquire a shared or exclusive lock on a table.
    """
    try:
        if lock_type == "shared":
            cursor.execute(f"LOCK TABLE {table_name} READ")
        elif lock_type == "exclusive":
            cursor.execute(f"LOCK TABLE {table_name} WRITE")
    except Error as e:
        print("Error acquiring lock:", e)

def release_lock(table_name):
    """
    Release the lock on a table.
    """
    try:
        cursor.execute(f"UNLOCK TABLES")
    except Error as e:
        print("Error releasing lock:", e)

def delete_product(product_id):
    """
    Delete a product with locking.
    """
    cursor.execute(f"SELECT * FROM Product WHERE Product_ID = '{product_id}'")
    product = cursor.fetchone()
    if not product:
        print(f"Product with ID {product_id} does not exist.")
        return
    acquire_lock("exclusive", "Product")

    try:
        cursor.execute(f"DELETE FROM Product WHERE Product_ID = '{product_id}'")
        conn.commit()
        print(f"Product {product_id} deleted successfully")
    except Error as e:
        conn.rollback()
        print("Error deleting product:", e)
    finally:
        release_lock("Product")

def update_product_info(product_id):
    cursor.execute(f"SELECT * FROM Product WHERE Product_ID = '{product_id}'")
    product = cursor.fetchone()
    if not product:
        print(f"Product with ID {product_id} does not exist.")
        return

    option = int(input("Enter option to update (1. Price/2. Quantity): "))

    
    """
    Update the quantity of a product with locking.
    """
    acquire_lock("exclusive", "Product")

    if option == 1:
        value = input(f"Enter new value for price: ")
        try:
            cursor.execute(f"UPDATE Product SET price = {value} WHERE Product_ID = '{product_id}'")
            conn.commit()
            print(f"Product {product_id} price updated to {value}")
        except Error as e:
            conn.rollback()
            print("Error updating product price:", e)
        finally:
            release_lock("Product")
    else:
        value = input(f"Enter new value for quantity: ")
        try:
            cursor.execute(f"UPDATE Product SET quantity = {value} WHERE Product_ID = '{product_id}'")
            conn.commit()
            print(f"Product {product_id} quantity updated to {value}")
        except Error as e:
            conn.rollback()
            print("Error updating product quantity:", e)
        finally:
            release_lock("Product")


def place_order(username, cart, total_quantity, total_amount, mode_of_payment):
    """
    Place a new order with locking.
    """
    try:

        

        cursor.execute("LOCK TABLES Product WRITE, Orders WRITE, ORDER_DETAILS WRITE, Payments Write, Makes Write, Delivers Write")
        

        
        for product_id in cart:
            cursor.execute(f"SELECT Price, Quantity FROM Product WHERE Product_ID = '{product_id}'")
            result = cursor.fetchone()

            
            if result is None:
                print(f"Product {product_id} not found")
                return
            
            available_quantity = result[1]
            if cart[product_id] > available_quantity:
                print(f"Not enough quantity available for {product_id}")
                total_amount -= result[0] * cart[product_id]
                return
            

            cursor.execute("UPDATE Product SET Quantity = Quantity - " + str(cart[product_id]) + " WHERE Product_ID = %s", (product_id,))

        cursor.execute("SELECT COUNT(DISTINCT Order_ID) AS Total_Unique_Orders FROM Orders;")
        number_order = cursor.fetchone()
        order_id = "ORD00" + str(number_order[0]+1)
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()
        for product_id in cart:
            cursor.execute("INSERT INTO Orders (Order_ID, Date1, Time1, No_of_books, Product_ID) VALUES (%s, %s, %s, %s, %s)", (order_id, current_date, current_time, cart[product_id], product_id))

        available_executives = find_available_executive()

        if available_executives:
            assign_order_to_executive(available_executives[0], order_id, username, total_quantity, total_amount)
        cursor.execute("SELECT COUNT(Payment_ID) AS Total_Unique_Payments FROM Payments;")
        number_payments = cursor.fetchone()
        payment_id = "PAY00" + str(number_payments[0]+1)
        cursor.execute("INSERT INTO Payments (Payment_ID, Amount, Order_ID, Mode_of_Payment) VALUES (%s, %s, %s, %s)", (payment_id, total_amount, order_id, mode_of_payment))
        cursor.execute("INSERT INTO Makes (Customer_ID, Payment_ID) VALUES (%s, %s)", (username, payment_id))

        

        conn.commit()

        print(f"Order {order_id} placed successfully for {total_quantity} units of {product_id}")

    except Error as e:
        conn.rollback()
        print("Error placing order:", e)

    finally:
        cursor.execute("UNLOCK TABLES")

update_product_info('1')
cart = dict()
cart['1'] = 2
place_order('cus001', cart, sum(cart.values()), 50.0, 'UPI')

 
while (True):
    print("1. Enter as a customer")
    print("2. Enter as admin")
    print("3. Enter as vendor")
    print("4. Enter as delivery executive")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    cart = dict()
    if choice == 1:
        print("1. Sign In\
              \n2. Sign Up")
        choice = int(input("choose your option: "))
        if choice == 1:
            flag, username = sign_in(conn)
            if (flag == 1):
                pass
            elif (flag == 0):
                continue
        else:
            sign_up(conn)
        while (True):
            print("1. View all the products\
                \n2. Search for a product\
                \n3. Search for the product based on a genre\
                \n4. Add a product to cart\
                \n5. Delete a product from cart\
                \n6. View cart\
                \n7. Purchase\
                \n8. View your orders and their status\
                \n9. View your transactions\
                \n10. update your information\
                \n11. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                cursor = conn.cursor()
                cursor.execute("SELECT * from Product")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 2:
                # cursor = conn.cursor()
                # product_name = input("Enter the name of the product: ")
                # cursor.execute("SELECT * from Product where name = %s", (product_name,))
                # rows = cursor.fetchall()
                # for row in rows:
                #     print(row)
                # cursor.close()
                # transaction 1 (non-conflicting)
                try:
                    cursor.execute("START TRANSACTION READ ONLY")
                    product_name = input("Enter the name of the product: ")
                    cursor.execute("SELECT * FROM Product WHERE Name = %s", (product_name,))
                    rows = cursor.fetchall()
                    if rows:
                        for row in rows:
                            print(row)
                    else:
                        print("Product not found.")
                    cursor.close()
                except Error as e:
                    print("Error retrieving product information:", e)
                    conn.rollback()
            elif choice == 3:
                genre_name = input("Enter the name of the genre: ")
                cursor = conn.cursor()
                cursor.execute("SELECT * from product where genre = %s", (genre_name,))
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 4:
                product_id = input("Enter the Product ID of the product to add to cart: ")
                quantity = int(input("Enter the quantity of the product to add to cart: "))
                if quantity <= 0 or quantity > 10:
                    print("Invalid quantity.")
                    continue
                if product_id in cart:
                    cart[product_id] += quantity
                else:
                    cart[product_id] = quantity
                print("Product added to cart.")
            elif choice == 5:
                if len(cart) == 0:
                    print("Your cart is empty.")
                    continue
                cursor = conn.cursor()
                for product_id in cart:
                    cursor.execute("SELECT Product_ID, Name, Ratings, Price, Genre FROM Product WHERE Product_ID = %s", (product_id,))
                    row = cursor.fetchone()
                    row += (cart[product_id],)
                    print(row)
                cursor.close()
                product_id = input("Enter the Product Id of the product you want to delete: ")
                quantity = int(input("Enter the quantity of the product you want to delete: "))
                if (product_id in cart):
                    if cart[product_id] > quantity:
                        cart[product_id] -= quantity
                    elif cart[product_id] == quantity:
                        cart.pop(product_id)
                    else:  
                        print("Invalid quantity.")
                        continue
                else:
                    print("Product does not exist in the cart.")
                    continue
                print("The product with the provided quantity has been removed from the cart.")
            elif choice == 6:
                if len(cart) == 0:
                    print("Your cart is empty.")
                else:
                    cursor = conn.cursor()
                    for product_id in cart:
                        cursor.execute("SELECT Product_ID, Name, Ratings, Price, Genre FROM Product WHERE Product_ID = %s", (product_id,))
                        row = cursor.fetchone()
                        row += (cart[product_id],)
                        print(row)
                    cursor.close()
            elif choice == 7:
                if len(cart) == 0:
                    print("Your cart is empty.")
                    continue
                bill = 0
                cursor = conn.cursor()
                for product_id in cart:
                    cursor.execute("SELECT Price FROM Product WHERE PRODUCT_ID = %s", (product_id,))
                    bill += (cart[product_id] * cursor.fetchone()[0])
                print("Bill: $", (bill))
                choice = str(input("Move ahead with the purchase?(y/n): "))
                if choice == 'y':
                    option = str(input("Choose a payment mode(\n1. Cash on Delivery\n2. UPI\n3. Credit Card\n4. Debit Card\n: "))
                    if option == '1':
                        mode_of_payment = "Cash on Delivery"
                    elif option == '2':
                        mode_of_payment = "UPI"
                    elif option == '3':
                        mode_of_payment = "Credit Card"
                    elif option == '4':
                        mode_of_payment = "Debit Card"
                    print("Bill Cleared!")
                    print("Here are the items you have purchased: ")
                    for product_id in cart:
                        cursor.execute("SELECT Product_ID, Name, Ratings, Price, Genre FROM Product WHERE Product_ID = %s", (product_id,))
                        row = cursor.fetchone()
                        row += (cart[product_id],)
                        print(row)
                    # for product_id in cart:
                    #     cursor.execute("UPDATE Product SET Quantity = Quantity - " + str(cart[product_id]) + " WHERE Product_ID = %s", (product_id,))
                    # cursor.execute("SELECT COUNT(DISTINCT Order_ID) AS Total_Unique_Orders FROM Orders;")
                    # number_order = cursor.fetchone()
                    # order_id = "ORD00" + str(number_order[0]+1)
                    # current_datetime = datetime.now()
                    # current_date = current_datetime.date()
                    # current_time = current_datetime.time()
                    # for product_id in cart:
                    #     cursor.execute("INSERT INTO Orders (Order_ID, Date1, Time1, No_of_books, Product_ID) VALUES (%s, %s, %s, %s, %s)", (order_id, current_date, current_time, cart[product_id], product_id))
                    # available_executives = find_available_executive()
                    # if available_executives:
                    #     assign_order_to_executive(available_executives[0], order_id, username, sum(cart.values()), bill)
                    # cursor.execute("SELECT COUNT(Payment_ID) AS Total_Unique_Payments FROM Payments;")
                    # number_payments = cursor.fetchone()
                    # payment_id = "PAY00" + str(number_payments[0]+1)
                    # cursor.execute("INSERT INTO Payments (Payment_ID, Amount, Order_ID, Mode_of_Payment) VALUES (%s, %s, %s, %s)", (payment_id, bill, order_id, mode_of_payment))
                    # cursor.execute("INSERT INTO Makes (Customer_ID, Payment_ID) VALUES (%s, %s)", (username, payment_id))
                    # conn.commit()
                    place_order(username, cart, sum(cart.values()), bill, mode_of_payment)
                    
                else:
                    print("You cannot move ahead with the purchase.")
                cursor.close()
            elif choice == 8:
                cursor = conn.cursor()
                cursor.execute("SELECT Order_id, Quantity, total_transaction_amount, CASE WHEN delivery_status = 0 THEN 'On the way' ELSE 'Delivered' END AS delivery_status FROM Order_details NATURAL JOIN Delivers WHERE Order_ID IN (SELECT Order_ID FROM Makes NATURAL JOIN Payments WHERE Customer_ID = %s)", (username,))
                orders = cursor.fetchall()
                for order in orders:
                    print(order)
                cursor.close()
            elif choice == 9:
                cursor = conn.cursor()
                cursor.execute("""SELECT OD.Order_ID, OD.Date1, OD.Time1, OD.No_of_books, OD.Product_ID, 
                    CF.Executive_ID AS Delivery_Executive, CF.Date_of_collection, CF.Time_of_collection, 
                    P.Amount AS Payment_Amount, P.Mode_of_Payment
                FROM Orders AS OD
                LEFT JOIN Collects_from AS CF ON OD.Order_ID = CF.Order_ID
                LEFT JOIN Payments AS P ON OD.Order_ID = P.Order_ID
                WHERE OD.Order_ID IN (SELECT Order_ID FROM Makes natural join payments WHERE Customer_ID = %s)
                """, (username,))
                transactions = cursor.fetchall()
                cursor.close()
                if transactions:
                    print("All Transactions:")
                    for transaction in transactions:
                        print("Order ID:", transaction[0])
                        print("Date:", transaction[1])
                        print("Time:", transaction[2])
                        print("No. of Books:", transaction[3])
                        print("Product ID:", transaction[4])
                        print("Payment Amount:", transaction[8])
                        print("Payment Mode:", transaction[9])
                        print("---------------------------")
                else:
                    print("No transactions found.")
            elif choice == 10:
                 # Transaction 2 (Non-Conflicting)
                try:
                    cursor.execute("START TRANSACTION")

                    new_contact_number = input("Enter new contact number: ")
                    new_house_no = input("Enter new house number: ")
                    new_street_no = input("Enter new street number: ")
                    new_zipcode = input("Enter new zipcode: ")
                    new_email_id = input("Enter new email ID: ")
                    new_age = input("Enter new age: ")
                    new_name_first = input("Enter new first name: ")
                    new_name_last = input("Enter new last name: ")

                    update_query = """
                        UPDATE Users
                        SET Contact_number = %s, House_No = %s, Street_no = %s, Zipcode = %s, Email_ID = %s, Age = %s,
                            Name_First_Name = %s, Name_Last_Name = %s
                        WHERE Customer_ID = %s
                    """

                    cursor.execute(update_query, (new_contact_number, new_house_no, new_street_no, new_zipcode, new_email_id,
                                                new_age, new_name_first, new_name_last, username))
                    conn.commit()

                    print("User information updated successfully!")
                except Error as e:
                    print("Error updating user information:", e)
                    conn.rollback()
            elif choice == 11:
                break
    elif choice == 2:
        username = admin_sign_in(conn)
        if username is None:
            continue
        while True:
            print("Admin Menu:")
            print("1. View all products")
            print("2. Purchase a product from the vendor inventory")
            print("3. View purchases with Vendors")
            print("4. Out of stock products")
            print("5. Update product information")
            print("6. Delete a product")
            print("7. View all orders")
            print("8. View all users")
            print("9. View all customer transactions")
            print("10. View low stock notifications")
            print("11. View all delivery executives")
            print("12. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Product")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 2:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM vendor_inventory")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                vendor_inventory_ID = input("Enter vendor inventory ID: ")
                quantity_to_purchase = int(input("Enter the quantity to purchase: "))
                
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM vendor_inventory WHERE vendor_inventory_ID = %s", (vendor_inventory_ID,))
                product = cursor.fetchone()
                
                if product:
                    available_quantity = product[4]
                    if available_quantity >= quantity_to_purchase:

                        total_cost = product[3] * quantity_to_purchase 

                        confirm_purchase = input(f"Total Cost: ${total_cost}. Confirm purchase? (y/n): ")
                        if confirm_purchase == 'y':

                            new_quantity = available_quantity - quantity_to_purchase
                            cursor.execute("UPDATE vendor_inventory SET Quantity = %s WHERE vendor_inventory_ID = %s", (new_quantity, vendor_inventory_ID))
                            conn.commit()
                            

                            current_date = datetime.now().date()
                            current_time = datetime.now().time()
                            cursor.execute("INSERT INTO Purchases_from(vendor_inventory_ID, username, Date_of_purchase, Time_of_purchase, Amount, Quantity) VALUES (%s, %s, %s, %s, %s, %s)",\
                                            (vendor_inventory_ID, username, current_date, current_time, total_cost, quantity_to_purchase))

                            conn.commit()
                            
                            print("Purchase successful!")
                        else:
                            print("Purchase cancelled.")
                    else:
                        print("Insufficient quantity in vendor_inventory.")
                else:
                    print("Product not found in vendor_inventory.")
            elif choice == 3:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Purchases_from")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 4:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM product_out_of_stock")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 5:
                product_id = input("Enter product ID to update: ")
                field = input("Enter field to update (Name/Ratings/Price/Quantity/Genre/Vendor_ID/Username): ")
                value = input(f"Enter new value for {field}: ")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE Product SET {field} = %s WHERE Product_ID = %s", (value, product_id))
                conn.commit()
                print("Product information updated successfully.")
                cursor.close()
            elif choice == 6:
                product_id = input("Enter product ID to delete: ")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Product WHERE Product_ID = %s", (product_id,))
                conn.commit()
                print("Product deleted successfully.")
                cursor.close()
            elif choice == 7:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Orders")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 8:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Users")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 9:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT OD.Order_ID, OD.Date1, OD.Time1, OD.No_of_books, OD.Product_ID, 
                        CF.Executive_ID AS Delivery_Executive, CF.Date_of_collection, CF.Time_of_collection, 
                        P.Amount AS Payment_Amount, P.Mode_of_Payment
                    FROM Orders AS OD
                    LEFT JOIN Collects_from AS CF ON OD.Order_ID = CF.Order_ID
                    LEFT JOIN Payments AS P ON OD.Order_ID = P.Order_ID
                """)
                transactions = cursor.fetchall()
                cursor.close()
                if transactions:
                    print("All Transactions:")
                    for transaction in transactions:
                        print("Order ID:", transaction[0])
                        print("Date:", transaction[1])
                        print("Time:", transaction[2])
                        print("No. of Books:", transaction[3])
                        print("Product ID:", transaction[4])
                        print("Payment Amount:", transaction[8])
                        print("Payment Mode:", transaction[9])
                        print("---------------------------")
                else:
                    print("No transactions found.")
            elif choice == 10:
                fetch_admin_notifications(conn)
            elif choice == 11:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Delivery_Executive")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                cursor.close()
            elif choice == 11:
                break
    elif choice == 3:
        print("1. Sign In")
        print("2. Sign Up")
        vendor_choice = int(input("Choose your option: "))
        if vendor_choice == 1:
            vendor_id = vendor_signin(conn)
            if vendor_id is None:
                continue
            while True:
                print("Vendor Menu:")
                print("1. Add Product to vendor_inventory")
                print("2. Add more quantity to existing product in vendor_inventory")
                print("3. Update your information")
                print("4. Exit")
                vendor_option = int(input("Choose your option: "))
                if vendor_option == 1:
                    # product_name = input("Enter book name: ")
                    # genre = input("Enter the genre: ")
                    # price = float(input("Enter product price: "))
                    # quantity = int(input("Enter product quantity: "))
                    # ratings = int(input("Enter product ratings: "))
                    
                    # cursor = conn.cursor()
                    # cursor.execute("INSERT INTO vendor_inventory (Book_Name, Vendor_ID, Price, Quantity, Genre, ratings) VALUES (%s, %s, %s, %s, %s, %s)",
                    #                 (product_name, vendor_id, price, quantity, genre, ratings))
                    # print("Product added to vendor_inventory successfully.")
                    
                    # conn.commit()
                    # cursor.close()
                    try:
                        cursor.execute("START TRANSACTION")


                        name = input("Enter product name: ")
                        ratings = int(input("Enter product ratings: "))
                        price = float(input("Enter product price: "))
                        quantity = int(input("Enter product quantity: "))
                        vendor_id = input("Enter vendor ID: ")
                        genre = input("Enter product genre: ")
                        


                        insert_query = """
                            INSERT INTO vendor_inventory(Book_Name, Vendor_ID,  Price, Quantity,  Genre, Ratings)
                            VALUES (%s, %s, %s, %s, %s, %s)
                        """


                        cursor.execute(insert_query, (name, vendor_id, price, quantity, genre, ratings))
                        conn.commit()

                        print("New product inserted successfully!")
                    except Error as e:
                        print("Error inserting new product:", e)
                        conn.rollback()
                elif vendor_option == 2:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM vendor_inventory WHERE Vendor_ID = %s", (vendor_id,))
                    products = cursor.fetchall()
                    for product in products:
                        print(product)
                    product_id = input("Enter product ID to update quantity: ")
                    quantity = int(input("Enter quantity to add: "))
                    cursor.execute("UPDATE vendor_inventory SET Quantity = Quantity + %s WHERE vendor_inventory_ID = %s", (quantity, product_id))
                    conn.commit()
                    cursor.close()
                elif vendor_option == 3:
                    #Transaction 4 (Non-Conflicting)
                    try:
                        cursor.execute("START TRANSACTION")
                        new_warehouse = input("Enter new warehouse: ")
                        new_street = input("Enter new street: ")
                        new_contact_number = input("Enter new contact number: ")
                        new_vendor_username = input("Enter new vendor username: ")
                        new_email_id = input("Enter new email ID: ")


                        update_query = """
                            UPDATE Vendor
                            SET Warehouse_no = %s, Street_no = %s, Contact_number = %s, Vendor_Username = %s, Email_ID = %s
                            WHERE Vendor_ID = %s
                        """


                        cursor.execute(update_query, (new_warehouse, new_street, new_contact_number, new_vendor_username, new_email_id, vendor_id))
                        conn.commit()

                        print("Vendor information updated successfully!")
                    except Error as e:
                        print("Error updating vendor information:", e)
                        conn.rollback()
                elif vendor_option == 3:
                    break
        elif vendor_choice == 2:
            vendor_signup(conn)
    elif choice == 4:
        print("1. Sign In")
        print("2. Sign Up")
        executive_choice = int(input("Choose your option: "))
        if executive_choice == 1:
            executive_id = delivery_executive_signin(conn)
            if executive_id is None:
                print("Invalid username or password. Please try again.")
                continue
            while True:
                print("Delivery Executive Menu:")
                print("1. View assigned orders")
                print("2. Mark order as delivered")
                print("3. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM Delivers WHERE Executive_ID = %s AND Delivery_Status = 0", (executive_id,))
                    assigned_orders = cursor.fetchall()
                    if assigned_orders:
                        print("Assigned Orders:")
                        for order in assigned_orders:
                            print(order)
                    else:
                        print("No assigned orders found.")
                    cursor.close()
                elif choice == 2:
                    order_id = input("Enter the order ID to mark as delivered: ")
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Delivers SET Delivery_Status = 1 WHERE Order_ID = %s AND Executive_ID = %s", (order_id, executive_id))
                    conn.commit()
                    cursor.close()
                    print("Order marked as delivered successfully.")
                elif choice == 3:
                    break
        elif executive_choice == 2:
            delivery_executive_signup(conn)
    elif choice == 5:
        print("Hope to see you again soon!")
        break
cursor.close()
conn.close()