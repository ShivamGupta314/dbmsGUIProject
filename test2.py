import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@shivam123",
            database="ecommerce"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to the database:", e)
        return None

# Function to close database connection
def close_connection(conn):
    if conn is not None and conn.is_connected():
        conn.close()

# Function to authenticate user
def authenticate(username, password):
    # You can implement your authentication logic here
    # For demonstration, let's assume a hardcoded username and password
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_window.destroy()  # Close login window
        open_main_window()  # Open main application window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open main window after successful login
def open_main_window():
    # Main window functionality goes here
    root = tk.Tk()
    root.title("E-commerce Management System")

    # Create buttons for different operations
    customer_button = tk.Button(root, text="Customer Operations", command=open_customer_window)
    customer_button.pack(pady=10)

    order_button = tk.Button(root, text="Order Operations", command=open_order_window)
    order_button.pack(pady=10)

    product_button = tk.Button(root, text="Product Operations", command=open_product_window)
    product_button.pack(pady=10)

    query_button = tk.Button(root, text="Execute Query", command=open_query_window)
    query_button.pack(pady=10)


# Function to execute SQL query
def execute_query(query_entry):
    query = query_entry.get()  # Get the query from the entry widget
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        show_result_window(cursor, result)  # Pass cursor to fetch column names
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to execute query: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to display query results in a new window with attribute names
def show_result_window(cursor, result):
    result_window = tk.Toplevel()
    result_window.title("Query Results")

    # Fetch column names from the cursor
    column_names = [description[0] for description in cursor.description]

    # Create a treeview widget to display the query results in a table format
    tree = ttk.Treeview(result_window)
    tree["columns"] = tuple(range(len(column_names)))  # Define columns based on the number of columns in the result

    # Add column headings
    for i, column_name in enumerate(column_names):
        tree.heading(i, text=column_name)

    # Add data rows
    for row in result:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=tk.YES, fill=tk.BOTH)

# Your existing code continues here...

# Function to insert customer into the database
def insert_customer(conn, data):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO customer (customer_id, customer_name, customer_phone, customer_email, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Customer inserted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to insert customer: {e}")
        conn.rollback()
    finally:
        cursor.close() 

# Function to delete customer from the database
def delete_customer(conn, customer_id):
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        conn.commit()
        messagebox.showinfo("Success", "Customer deleted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to delete customer: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to update customer details in the database
def update_customer(conn, data):
    cursor = conn.cursor()
    try:
        sql = "UPDATE customer SET customer_name = %s, customer_phone = %s, customer_email = %s, address = %s WHERE customer_id = %s"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Customer updated successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to update customer: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to insert customer into the database
def insert_customer(conn, data):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO customer (customer_id, customer_name, customer_phone, customer_email, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Customer inserted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to insert customer: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to delete customer from the database
def delete_customer(conn, customer_id):
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(sql, (customer_id,))
        conn.commit()
        messagebox.showinfo("Success", "Customer deleted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to delete customer: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to update customer details in the database
def update_customer(conn, data):
    cursor = conn.cursor()
    try:
        sql = "UPDATE customer SET customer_name = %s, customer_phone = %s, customer_email = %s, address = %s WHERE customer_id = %s"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Customer updated successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to update customer: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to insert order into the database
def insert_order(conn, data):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO orders (order_id,order_date, total_order_value, delivery_date, customer_id, supplier_id) VALUES (%s, %s,%s, %s, %s, %s)"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Order inserted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to insert order: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to delete order from the database
def delete_order(conn, order_id):
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM orders WHERE order_id = %s"
        cursor.execute(sql, (order_id,))
        conn.commit()
        messagebox.showinfo("Success", "Order deleted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to delete order: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to update order details in the database
def update_order(conn, data):
    cursor = conn.cursor()
    try:
        sql = "UPDATE orders SET total_order_value = %s, delivery_date = %s, customer_id = %s, supplier_id = %s WHERE order_id = %s"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Order updated successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to update order: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to insert product into the database
def insert_product(conn, data):
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO product (product_id,product_name, brand, product_domain, quantity, supplier_id, order_id) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Product inserted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to insert product: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to delete product from the database
def delete_product(conn, product_id):
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM product WHERE product_id = %s"
        cursor.execute(sql, (product_id,))
        conn.commit()
        messagebox.showinfo("Success", "Product deleted successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to delete product: {e}")
        conn.rollback()
    finally:
        cursor.close()

# Function to update product details in the database
def update_product(conn, data):
    cursor = conn.cursor()
    try:
        sql = "UPDATE product SET product_name = %s, brand = %s, product_domain = %s, quantity = %s, supplier_id = %s, order_id = %s WHERE product_id = %s"
        cursor.execute(sql, data)
        conn.commit()
        messagebox.showinfo("Success", "Product updated successfully")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Failed to update product: {e}")
        conn.rollback()
    finally:
        cursor.close()

   


# Function to open delete customer window
def open_delete_customer_window():
    delete_customer_window = tk.Toplevel()
    delete_customer_window.title("Delete Customer")

    delete_customer_frame = tk.LabelFrame(delete_customer_window, text="Delete Customer")
    delete_customer_frame.pack(padx=10, pady=10)

    customer_id_label = tk.Label(delete_customer_frame, text="Customer ID:")
    customer_id_label.grid(row=0, column=0, padx=5, pady=5)
    customer_id_entry = tk.Entry(delete_customer_frame)
    customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_customer_action():
        customer_id = customer_id_entry.get()
        conn = connect_to_database()
        if conn:
            delete_customer(conn, customer_id)
            close_connection(conn)
            delete_customer_window.destroy()

    delete_button = tk.Button(delete_customer_frame, text="Delete", command=delete_customer_action)
    delete_button.grid(row=1, column=0, columnspan=2, pady=5)

# Function to open delete order window
def open_delete_order_window():
    delete_order_window = tk.Toplevel()
    delete_order_window.title("Delete Order")

    delete_order_frame = tk.LabelFrame(delete_order_window, text="Delete Order")
    delete_order_frame.pack(padx=10, pady=10)

    order_id_label = tk.Label(delete_order_frame, text="Order ID:")
    order_id_label.grid(row=0, column=0, padx=5, pady=5)
    order_id_entry = tk.Entry(delete_order_frame)
    order_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_order_action():
        order_id = order_id_entry.get()
        conn = connect_to_database()
        if conn:
            delete_order(conn, order_id)
            close_connection(conn)
            delete_order_window.destroy()

    delete_button = tk.Button(delete_order_frame, text="Delete", command=delete_order_action)
    delete_button.grid(row=1, column=0, columnspan=2, pady=5)

# Function to open delete product window
def open_delete_product_window():
    delete_product_window = tk.Toplevel()
    delete_product_window.title("Delete Product")

    delete_product_frame = tk.LabelFrame(delete_product_window, text="Delete Product")
    delete_product_frame.pack(padx=10, pady=10)

    product_id_label = tk.Label(delete_product_frame, text="Product ID:")
    product_id_label.grid(row=0, column=0, padx=5, pady=5)
    product_id_entry = tk.Entry(delete_product_frame)
    product_id_entry.grid(row=0, column=1, padx=5, pady=5)

    def delete_product_action():
        product_id = product_id_entry.get()
        conn = connect_to_database()
        if conn:
            delete_product(conn, product_id)
            close_connection(conn)
            delete_product_window.destroy()

    delete_button = tk.Button(delete_product_frame, text="Delete", command=delete_product_action)
    delete_button.grid(row=1, column=0, columnspan=2, pady=5)

# Function to create customer window
def open_customer_window():
    customer_window = tk.Toplevel()
    customer_window.title("Customer Operations")

    # Create customer section
    customer_frame = tk.LabelFrame(customer_window, text="Customer Operations")
    customer_frame.pack(padx=10, pady=10)

    # Create customer entry fields
    customer_id_label = tk.Label(customer_frame, text="Customer ID:")
    customer_id_label.grid(row=0, column=0, padx=5, pady=5)
    customer_id_entry = tk.Entry(customer_frame)
    customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

    customer_name_label = tk.Label(customer_frame, text="Name:")
    customer_name_label.grid(row=1, column=0, padx=5, pady=5)
    customer_name_entry = tk.Entry(customer_frame)
    customer_name_entry.grid(row=1, column=1, padx=5, pady=5)

    customer_phone_label = tk.Label(customer_frame, text="Phone:")
    customer_phone_label.grid(row=2, column=0, padx=5, pady=5)
    customer_phone_entry = tk.Entry(customer_frame)
    customer_phone_entry.grid(row=2, column=1, padx=5, pady=5)

    customer_email_label = tk.Label(customer_frame, text="Email:")
    customer_email_label.grid(row=3, column=0, padx=5, pady=5)
    customer_email_entry = tk.Entry(customer_frame)
    customer_email_entry.grid(row=3, column=1, padx=5, pady=5)

    customer_address_label = tk.Label(customer_frame, text="Address:")
    customer_address_label.grid(row=4, column=0, padx=5, pady=5)
    customer_address_entry = tk.Entry(customer_frame)
    customer_address_entry.grid(row=4, column=1, padx=5, pady=5)

    # Function to add customer
    def add_customer():
        customer_id = customer_id_entry.get()
        name = customer_name_entry.get()
        phone = customer_phone_entry.get()
        email = customer_email_entry.get()
        address = customer_address_entry.get()
        data = (customer_id, name, phone, email, address)
        conn = connect_to_database()
        if conn:
            insert_customer(conn, data)
            close_connection(conn)

    add_customer_button = tk.Button(customer_frame, text="Add Customer", command=add_customer)
    add_customer_button.grid(row=5, column=0, columnspan=2, pady=5)

    # Function to update customer
    def update_customer_action():
        customer_id = customer_id_entry.get()
        name = customer_name_entry.get()
        phone = customer_phone_entry.get()
        email = customer_email_entry.get()
        address = customer_address_entry.get()
        data = (name, phone, email, address, customer_id)
        conn = connect_to_database()
        if conn:
            update_customer(conn, data)
            close_connection(conn)

    update_customer_button = tk.Button(customer_frame, text="Update Customer", command=update_customer_action)
    update_customer_button.grid(row=6, column=0, columnspan=2, pady=5)

    # Function to open delete customer window
    delete_customer_button = tk.Button(customer_frame, text="Delete Customer", command=open_delete_customer_window)
    delete_customer_button.grid(row=7, column=0, columnspan=2, pady=5)

# Function to create order window
def open_order_window():
    order_window = tk.Toplevel()
    order_window.title("Order Operations")

    # Create order section
    order_frame = tk.LabelFrame(order_window, text="Order Operations")
    order_frame.pack(padx=10, pady=10)

    # Create order entry fields
    order_id_label = tk.Label(order_frame, text="Order ID:")
    order_id_label.grid(row=0, column=0, padx=5, pady=5)
    order_id_entry = tk.Entry(order_frame)
    order_id_entry.grid(row=0, column=1, padx=5, pady=5)

    order_date_label = tk.Label(order_frame, text="Order Date:")
    order_date_label.grid(row=1, column=0, padx=5, pady=5)
    order_date_entry = tk.Entry(order_frame)
    order_date_entry.grid(row=1, column=1, padx=5, pady=5)

    total_order_value_label = tk.Label(order_frame, text="Total Order Value:")
    total_order_value_label.grid(row=2, column=0, padx=5, pady=5)
    total_order_value_entry = tk.Entry(order_frame)
    total_order_value_entry.grid(row=2, column=1, padx=5, pady=5)

    delivery_date_label = tk.Label(order_frame, text="Delivery Date:")
    delivery_date_label.grid(row=3, column=0, padx=5, pady=5)
    delivery_date_entry = tk.Entry(order_frame)
    delivery_date_entry.grid(row=3, column=1, padx=5, pady=5)

    customer_id_label = tk.Label(order_frame, text="Customer ID:")
    customer_id_label.grid(row=4, column=0, padx=5, pady=5)
    customer_id_entry = tk.Entry(order_frame)
    customer_id_entry.grid(row=4, column=1, padx=5, pady=5)

    supplier_id_label = tk.Label(order_frame, text="Supplier ID:")
    supplier_id_label.grid(row=5, column=0, padx=5, pady=5)
    supplier_id_entry = tk.Entry(order_frame)
    supplier_id_entry.grid(row=5, column=1, padx=5, pady=5)

    # Function to add order
    def add_order():
        order_id = order_id_entry.get()
        order_date = order_date_entry.get()
        total_order_value = total_order_value_entry.get()
        delivery_date = delivery_date_entry.get()
        customer_id = customer_id_entry.get()
        supplier_id = supplier_id_entry.get()
        data = (order_id, order_date, total_order_value, delivery_date, customer_id, supplier_id)
        conn = connect_to_database()
        if conn:
            insert_order(conn, data)
            close_connection(conn)

    add_order_button = tk.Button(order_frame, text="Add Order", command=add_order)
    add_order_button.grid(row=6, column=0, columnspan=2, pady=5)

    # Function to update order
    def update_order_action():
        order_id = order_id_entry.get()
        total_order_value = total_order_value_entry.get()
        delivery_date = delivery_date_entry.get()
        customer_id = customer_id_entry.get()
        supplier_id = supplier_id_entry.get()
        data = (total_order_value, delivery_date, customer_id, supplier_id, order_id)
        conn = connect_to_database()
        if conn:
            update_order(conn, data)
            close_connection(conn)

    update_order_button = tk.Button(order_frame, text="Update Order", command=update_order_action)
    update_order_button.grid(row=7, column=0, columnspan=2, pady=5)

    # Function to open delete order window
    delete_order_button = tk.Button(order_frame, text="Delete Order", command=open_delete_order_window)
    delete_order_button.grid(row=8, column=0, columnspan=2, pady=5)

# Function to create product window
def open_product_window():
    product_window = tk.Toplevel()
    product_window.title("Product Operations")

    # Create product section
    product_frame = tk.LabelFrame(product_window, text="Product Operations")
    product_frame.pack(padx=10, pady=10)

    # Create product entry fields
    product_id_label = tk.Label(product_frame, text="Product ID:")
    product_id_label.grid(row=0, column=0, padx=5, pady=5)
    product_id_entry = tk.Entry(product_frame)
    product_id_entry.grid(row=0, column=1, padx=5, pady=5)

    product_name_label = tk.Label(product_frame, text="Product Name:")
    product_name_label.grid(row=1, column=0, padx=5, pady=5)
    product_name_entry = tk.Entry(product_frame)
    product_name_entry.grid(row=1, column=1, padx=5, pady=5)

    brand_label = tk.Label(product_frame, text="Brand:")
    brand_label.grid(row=2, column=0, padx=5, pady=5)
    brand_entry = tk.Entry(product_frame)
    brand_entry.grid(row=2, column=1, padx=5, pady=5)

    product_domain_label = tk.Label(product_frame, text="Product Domain:")
    product_domain_label.grid(row=3, column=0, padx=5, pady=5)
    product_domain_entry = tk.Entry(product_frame)
    product_domain_entry.grid(row=3, column=1, padx=5, pady=5)

    quantity_label = tk.Label(product_frame, text="Quantity:")
    quantity_label.grid(row=4, column=0, padx=5, pady=5)
    quantity_entry = tk.Entry(product_frame)
    quantity_entry.grid(row=4, column=1, padx=5, pady=5)

    supplier_id_label = tk.Label(product_frame, text="Supplier ID:")
    supplier_id_label.grid(row=5, column=0, padx=5, pady=5)
    supplier_id_entry = tk.Entry(product_frame)
    supplier_id_entry.grid(row=5, column=1, padx=5, pady=5)

    order_id_label = tk.Label(product_frame, text="Order ID:")
    order_id_label.grid(row=6, column=0, padx=5, pady=5)
    order_id_entry = tk.Entry(product_frame)
    order_id_entry.grid(row=6, column=1, padx=5, pady=5)

    # Function to add product
    def add_product():
        product_id = product_id_entry.get()
        product_name = product_name_entry.get()
        brand = brand_entry.get()
        product_domain = product_domain_entry.get()
        quantity = quantity_entry.get()
        supplier_id = supplier_id_entry.get()
        order_id = order_id_entry.get()
        data = (product_id, product_name, brand, product_domain, quantity, supplier_id, order_id)
        conn = connect_to_database()
        if conn:
            insert_product(conn, data)
            close_connection(conn)

    add_product_button = tk.Button(product_frame, text="Add Product", command=add_product)
    add_product_button.grid(row=7, column=0, columnspan=2, pady=5)

    # Function to update product
    def update_product_action():
        product_id = product_id_entry.get()
        product_name = product_name_entry.get()
        brand = brand_entry.get()
        product_domain = product_domain_entry.get()
        quantity = quantity_entry.get()
        supplier_id = supplier_id_entry.get()
        order_id = order_id_entry.get()
        data = (product_name, brand, product_domain, quantity, supplier_id, order_id, product_id)
        conn = connect_to_database()
        if conn:
            update_product(conn, data)
            close_connection(conn)

    update_product_button = tk.Button(product_frame, text="Update Product", command=update_product_action)
    update_product_button.grid(row=8, column=0, columnspan=2, pady=5)

    # Function to open delete product window
    delete_product_button = tk.Button(product_frame, text="Delete Product", command=open_delete_product_window)
    delete_product_button.grid(row=9, column=0, columnspan=2, pady=5)




# Function to open query window
def open_query_window():
    root = tk.Tk()
    root.title("Execute Query")

    query_frame = tk.LabelFrame(root, text="Execute SQL Query")
    query_frame.pack(padx=10, pady=10)

    query_label = tk.Label(query_frame, text="Enter your SQL Query:")
    query_label.grid(row=0, column=0, padx=5, pady=5)
    query_entry = tk.Entry(query_frame, width=50)
    query_entry.grid(row=0, column=1, padx=5, pady=5)

    execute_button = tk.Button(query_frame, text="Execute", command=lambda: execute_query(query_entry))
    execute_button.grid(row=0, column=2, padx=5, pady=5)

    root.mainloop()

# Main login window
login_window = tk.Tk()
login_window.title("Login")

# Username label and entry field
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

# Password label and entry field
password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

login_window.mainloop()