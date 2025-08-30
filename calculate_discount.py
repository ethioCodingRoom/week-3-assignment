# Calculate the discount amount based on the original price and discount percentage
def calculate_discount(price, discount_percentage):
    # Calculate the discount amount after applying the discount percentage
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    


# Main part of the program getting user input and calculating the final price
if __name__ == "__main__":
    try:
        # Asking user for input
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(original_price, discount_percentage)

        if discount_percentage >= 20:
            print(f"The final price after discount is: {final_price}")
        else:
            print(f"No discount applied: The original price is: {original_price}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

