import products
import store


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)

    while True:
        print("\n===== STORE MENU =====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n--- Product List ---")
            for i, product in enumerate(best_buy.get_all_products()):
                print(f"{i + 1}. {product.name}, Price: {product.formatted_price}, Quantity: {product.quantity}")

        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"\nTotal amount of items in store: {total}")

        elif choice == "3":
            products_list = best_buy.get_all_products()
            shopping_list = []

            print("\n--- Available Products ---")
            for i, product in enumerate(products_list):
                print(f"{i + 1}. {product.name} (Price: {product.formatted_price}, Quantity: {product.quantity})")

            while True:
                product_input = input("Enter product number (or 'done' to finish): ")

                if product_input.lower() == "done":
                    break

                try:
                    product_index = int(product_input) - 1
                    product = products_list[product_index]

                    quantity = int(input("Enter quantity: "))

                    shopping_list.append((product, quantity))

                except (ValueError, IndexError):
                    print("Invalid input, try again.")

            try:
                total_price = best_buy.order(shopping_list)
                print(f"\nOrder successful! Total price: {total_price}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()