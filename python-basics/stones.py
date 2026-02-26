# Machine Cut Stones POS System
# Date: 24/02/2026

def calculate_total(qty_6, qty_9, qty_reject, price_6, price_9, price_reject):
    total_6 = qty_6 * price_6
    total_9 = qty_9 * price_9
    total_reject = qty_reject * price_reject
    grand_total = total_6 + total_9 + total_reject
    return total_6, total_9, total_reject, grand_total


def main():
    print("===== MACHINE CUT STONES POS =====\n")

    customer = input("Enter customer name: ")

    # Prices (you can change these)
    price_6 = float(input("Enter price per stone (Prime 6\"): "))
    price_9 = float(input("Enter price per stone (Prime 9\"): "))
    price_reject = float(input("Enter price per stone (Reject): "))

    print("\nEnter quantities sold")
    qty_6 = int(input("Prime 6\" quantity: "))
    qty_9 = int(input("Prime 9\" quantity: "))
    qty_reject = int(input("Reject quantity: "))

    total_6, total_9, total_reject, grand_total = calculate_total(
        qty_6, qty_9, qty_reject, price_6, price_9, price_reject
    )

    print("\n======= RECEIPT =======")
    print(f"Customer: {customer}")
    print("------------------------")
    print(f"Prime 6\"  : {qty_6} x {price_6:,.2f} = {total_6:,.2f}")
    print(f"Prime 9\"  : {qty_9} x {price_9:,.2f} = {total_9:,.2f}")
    print(f"Reject     : {qty_reject} x {price_reject:,.2f} = {total_reject:,.2f}")
    print("------------------------")
    print(f"TOTAL: {grand_total:,.2f}")
    print("========================")


if __name__ == "__main__":
    main()