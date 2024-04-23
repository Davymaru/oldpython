def main():
    try:
        with open("sales_totals.txt", "r") as file:
            total = 0.0
            count = 0

            for line in file:
                sales_amount = float(line.strip())
                total += sales_amount
                count += 1
                print(f"${sales_amount:,.2f}")

            print(f"\nTotal: ${total:,.2f}")
            print(f"Count: {count}")

            if count != 0:
                print(f"Average: ${total / count:,.2f}")
            else:
                print("Average: N/A (count is zero)")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
