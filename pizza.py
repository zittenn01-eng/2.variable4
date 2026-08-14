# [Chapter 2]
# Pizza Menu
pizza1 = "Pepperoni Pizza"
pizza2 = "Cheese Pizza"
pizza3 = "Combination Pizza"
pizza4 = "Bulgogi Pizza"
pizza5 = "Seafood Pizza"
price1 = 4000

# Select Pizza
print("Select Pizza")
print(pizza1, "(", price1, ")")
print(pizza2, "(", price1, ")")
print(pizza3, "(", price1, ")")
print(pizza4, "(", price1, ")")
print(pizza5, "(", price1, ")")

pizza = input("Enter Pizza: ")
pizza_count = int(input("Enter Qty: "))
total_price = 0

print("===========================")
print("Receipt:")
print("===========================")
print("Pizza:")

subtotal = price1 * pizza_count
total_price = total_price + subtotal

print("-", pizza, "(", price1, ") x", pizza_count)
print("---------------------------")
print("Total Price:", subtotal)
drink1 = "Coke"
drink2 = "Cider"
drink_price = 2000