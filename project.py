import tkinter as tk
from tkinter import messagebox

class RestaurantManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Food and Order Management")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f5f5dc")

        self.menu = {
            1: ("Pizza", 10.0),
            2: ("Burger", 5.0),
            3: ("Pasta", 7.0),
            4: ("Salad", 4.0),
            5: ("Sushi", 12.0),
            6: ("Tacos", 8.0),
            7: ("Steak", 15.0),
            8: ("Ice Cream", 3.0),
            9: ("Coffee", 2.5),
            10: ("Tea", 2.0)
        }
        self.cart = {}
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Restaurant Food And Order Management System", font=("Arial", 22, "bold"), bg="#f5f5dc", pady=20).pack()

        main_frame = tk.Frame(self.root, bg="#f5f5dc")
        main_frame.pack(expand=True, pady=10)

        left_frame = tk.Frame(main_frame, bd=3, relief=tk.GROOVE, bg="#d0e8f2")
        left_frame.grid(row=0, column=0, padx=50, pady=10)

        right_frame = tk.Frame(main_frame, bd=3, relief=tk.GROOVE, bg="#d0e8f2")
        right_frame.grid(row=0, column=1, padx=50, pady=10)

        tk.Label(left_frame, text="Menu", font=("Arial", 18, "bold"), bg="#d0e8f2").grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_listbox = tk.Listbox(left_frame, width=45, height=16, font=("Arial", 14), bg="#f0f8ff")
        self.menu_listbox.grid(row=1, column=0, columnspan=2, pady=10)
        self.update_menu_listbox()

        tk.Label(left_frame, text="Search by ID:", font=("Arial", 12), bg="#d0e8f2").grid(row=2, column=0, pady=5, sticky="e")
        self.search_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.search_entry.grid(row=2, column=1, pady=5, sticky="w")
        tk.Button(left_frame, text="Search", command=self.search_item, font=("Arial", 12), bg="#a3d2ca").grid(row=3, column=0, columnspan=2, pady=5)

        tk.Label(left_frame, text="Name:", font=("Arial", 12), bg="#d0e8f2").grid(row=4, column=0, pady=5, sticky="e")
        self.item_name_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.item_name_entry.grid(row=4, column=1, pady=5, sticky="w")

        tk.Label(left_frame, text="Price:", font=("Arial", 12), bg="#d0e8f2").grid(row=5, column=0, pady=5, sticky="e")
        self.item_price_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.item_price_entry.grid(row=5, column=1, pady=5, sticky="w")

        tk.Button(left_frame, text="Add Item", command=self.add_item, font=("Arial", 12), bg="#a3d2ca").grid(row=6, column=0, columnspan=2, pady=5)
        tk.Button(left_frame, text="Delete Item", command=self.delete_item, font=("Arial", 12), bg="#a3d2ca").grid(row=7, column=0, columnspan=2, pady=5)

        tk.Label(right_frame, text="Cart", font=("Arial", 18, "bold"), bg="#d0e8f2").grid(row=0, column=0, columnspan=2, pady=10)

        self.cart_listbox = tk.Listbox(right_frame, width=45, height=16, font=("Arial", 14), bg="#f0f8ff")
        self.cart_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(right_frame, text="Quantity:", font=("Arial", 12), bg="#d0e8f2").grid(row=2, column=0, pady=5, sticky="e")
        self.quantity_entry = tk.Entry(right_frame, font=("Arial", 12), width=15)
        self.quantity_entry.grid(row=2, column=1, pady=5, sticky="w")

        tk.Button(right_frame, text="Add to Cart", command=self.add_to_cart, font=("Arial", 12), bg="#a3d2ca").grid(row=3, column=0, columnspan=2, pady=5)
        tk.Button(right_frame, text="Remove from Cart", command=self.remove_from_cart, font=("Arial", 12), bg="#a3d2ca").grid(row=4, column=0, columnspan=2, pady=5)
        tk.Button(right_frame, text="Generate Bill", command=self.generate_bill, font=("Arial", 12), bg="#a3d2ca").grid(row=5, column=0, columnspan=2, pady=5)

        self.bill_label = tk.Label(right_frame, text="Total Bill: $0.0", font=("Arial", 14, "bold"), bg="#d0e8f2")
        self.bill_label.grid(row=6, column=0, columnspan=2, pady=10)

    def update_menu_listbox(self):
        self.menu_listbox.delete(0, tk.END)
        for item_id, (item, price) in self.menu.items():
            self.menu_listbox.insert(tk.END, f"{item_id}. {item} - ${price}")

    def search_item(self):
        query = self.search_entry.get().strip()
        if not query:
            self.update_menu_listbox()
            return
        if not query.isdigit():
            messagebox.showerror("Error", "Please enter a valid ID.")
            return
        query = int(query)
        self.menu_listbox.delete(0, tk.END)
        if query in self.menu:
            item, price = self.menu[query]
            self.menu_listbox.insert(tk.END, f"{query}. {item} - ${price}")
        else:
            messagebox.showinfo("Not Found", "No item found with the given ID.")

    def add_item(self):
        name = self.item_name_entry.get().strip()
        price = self.item_price_entry.get().strip()
        if not name or not price:
            messagebox.showerror("Error", "Both name and price are required.")
            return
        if any(item_name.lower() == name.lower() for _, (item_name, _) in self.menu.items()):
            messagebox.showerror("Error", f"Item '{name}' already exists in the menu.")
            return
        try:
            price = float(price)
            new_id = max(self.menu.keys(), default=0) + 1
            self.menu[new_id] = (name, price)
            self.update_menu_listbox()
            messagebox.showinfo("Success", f"{name} added to the menu with ID {new_id}.")
        except ValueError:
            messagebox.showerror("Error", "Price must be a valid number.")

    def delete_item(self):
        selected = self.menu_listbox.curselection()
        if selected:
            item_text = self.menu_listbox.get(selected)
            item_id = int(item_text.split(".")[0])
            del self.menu[item_id]
            self.update_menu_listbox()
            messagebox.showinfo("Success", f"Item ID {item_id} removed from the menu.")
        else:
            messagebox.showerror("Error", "No item selected.")

    def add_to_cart(self):
        selected = self.menu_listbox.curselection()
        if selected:
            item_text = self.menu_listbox.get(selected)
            item_id = int(item_text.split(".")[0])
            try:
                quantity = int(self.quantity_entry.get())
                if quantity > 0:
                    self.cart[item_id] = self.cart.get(item_id, 0) + quantity
                    self.update_cart_listbox()
                else:
                    messagebox.showerror("Error", "Quantity must be greater than 0.")
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a number.")

    def update_cart_listbox(self):
        self.cart_listbox.delete(0, tk.END)
        for item_id, quantity in self.cart.items():
            item_name, price = self.menu[item_id]
            self.cart_listbox.insert(tk.END, f"{item_name} - {quantity} x ${price}")

    def remove_from_cart(self):
        selected = self.cart_listbox.curselection()
        if selected:
            item_text = self.cart_listbox.get(selected)
            item_name = item_text.split(" - ")[0]
            item_id = next((id for id, data in self.menu.items() if data[0] == item_name), None)
            if item_id and item_id in self.cart:
                del self.cart[item_id]
                self.update_cart_listbox()
        else:
            messagebox.showerror("Error", "No item selected.")

    def generate_bill(self):
        total = sum(self.cart[item_id] * self.menu[item_id][1] for item_id in self.cart)
        self.bill_label.config(text=f"Total Bill: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantManagement(root)
    root.mainloop()
