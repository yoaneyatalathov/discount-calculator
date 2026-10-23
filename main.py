
import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        price = float(price_entry.get())
        discount_rate = float(discount_entry.get())
        quantity = int(quantity_entry.get())

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        if not 0 <= discount_rate <= 100:
            raise ValueError("Discount must be between 0 and 100.")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        subtotal = price * quantity
        discount_amount = subtotal * discount_rate / 100
        final_total = subtotal - discount_amount

        subtotal_label.config(text=f"Rp {subtotal:,.2f}")
        discount_label.config(text=f"Rp {discount_amount:,.2f}")
        total_label.config(text=f"Rp {final_total:,.2f}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter a valid price, discount (0-100), and quantity."
        )


def reset_form():
    price_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    subtotal_label.config(text="Rp 0.00")
    discount_label.config(text="Rp 0.00")
    total_label.config(text="Rp 0.00")


# Main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("480x650")
root.minsize(420, 580)
root.resizable(True, True)
root.configure(bg="#F3F6FA")

# Heading
tk.Label(
    root,
    text="Discount Calculator",
    font=("Segoe UI", 20, "bold"),
    bg="#F3F6FA",
    fg="#172554"
).pack(pady=(20, 5))

tk.Label(
    root,
    text="Calculate your purchase total",
    font=("Segoe UI", 10),
    bg="#F3F6FA",
    fg="#64748B"
).pack(pady=(0, 20))

# Input section
form = tk.Frame(root, bg="white", padx=20, pady=15)
form.pack(fill="x", padx=25)

def add_input(label_text):
    tk.Label(
        form,
        text=label_text,
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="#334155"
    ).pack(anchor="w", pady=(8, 4))

    entry = tk.Entry(
        form,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    entry.pack(fill="x", ipady=5)
    return entry


price_entry = add_input("Price per item (Rp)")
discount_entry = add_input("Discount (%)")
quantity_entry = add_input("Quantity")

# Buttons
button_frame = tk.Frame(root, bg="#F3F6FA")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Calculate",
    command=calculate_discount,
    font=("Segoe UI", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_form,
    font=("Segoe UI", 10, "bold"),
    bg="#E2E8F0",
    fg="#334155",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

# Results section
results = tk.Frame(root, bg="white", padx=20, pady=12)
results.pack(fill="x", padx=25, pady=(0, 20))

def add_result(label_text, is_total=False):
    row = tk.Frame(results, bg="white")
    row.pack(fill="x", pady=5)

    tk.Label(
        row,
        text=label_text,
        font=("Segoe UI", 10, "bold" if is_total else "normal"),
        bg="white",
        fg="#172554" if is_total else "#64748B"
    ).pack(side="left")

    value = tk.Label(
        row,
        text="Rp 0.00",
        font=("Segoe UI", 11, "bold" if is_total else "normal"),
        bg="white",
        fg="#16A34A" if is_total else "#334155"
    )
    value.pack(side="right")
    return value


subtotal_label = add_result("Subtotal")
discount_label = add_result("Discount Amount")
total_label = add_result("Final Payment", is_total=True)

# Start application
root.mainloop()