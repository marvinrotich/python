def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after applying the discount: ${:.2f}".format(final_price))
