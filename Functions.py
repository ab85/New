def calculate_order_total(items, discount_percent=0, free_shipping_limit=50, shipping_fee=5):
	"""Calculate an order total for an online store.

	items must be a list of dictionaries with name, price, and quantity.
	"""
	if not items:
		raise ValueError("The order must contain at least one item")

	subtotal = 0

	for item in items:
		if item["price"] < 0 or item["quantity"] <= 0:
			raise ValueError("Price cannot be negative and quantity must be positive")

		subtotal += item["price"] * item["quantity"]

	discount = subtotal * (discount_percent / 100)
	shipping = 0 if subtotal >= free_shipping_limit else shipping_fee
	total = subtotal - discount + shipping

	return {
		"subtotal": subtotal,
		"discount": discount,
		"shipping": shipping,
		"total": total,
	}


shopping_cart = []
number_of_items = int(input("How many different products? "))

for item_number in range(number_of_items):
	print(f"\nProduct {item_number + 1}")
	name = input("Product name: ")
	price = float(input("Price: "))
	quantity = int(input("Quantity: "))

	shopping_cart.append({
		"name": name,
		"price": price,
		"quantity": quantity,
	})

discount_percent = float(input("Discount percentage: "))
free_shipping_limit = float(input("Free shipping for orders over: "))
shipping_fee = float(input("Shipping fee: "))
order = calculate_order_total(
	shopping_cart,
	discount_percent,
	free_shipping_limit,
	shipping_fee,
)

print(f"Subtotal: ${order['subtotal']:.2f}")
print(f"Discount: ${order['discount']:.2f}")
print(f"Shipping: ${order['shipping']:.2f}")
print(f"Total: ${order['total']:.2f}")
