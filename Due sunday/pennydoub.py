"""
    Recursive function to calculate the amount of money when a penny is doubled every day.

    :param days: int - The number of days over which the penny is doubled.
    :param amount: float - The current amount of money. Default is 0.01, representing 1 penny.
    :return: float - The total amount of money after the specified number of days.
"""


def double_penny(days, amount=0.01):
    if days == 1:
        return amount
    else:
        return double_penny(days - 1, amount * 2)

def main():
    # Example usage
    days = int(input("Enter the number of days: "))
    total_amount = double_penny(days)
    print(f"Total amount after {days} days: ${total_amount:,.2f}")

main()
