class ShoppingCart(object):
	def __init__(self):
		self.total = 0
		self.items = {}

	def add_item(self, item_name, quantity, price):
		if item_name not in self.items:
			self.items[item_name] = quantity 
			self.total += (quantity * price)
			print ("{} {} added to cart".format(quantity, item_name))
			print (self.items)
			return "Total amount: {}".format(self.total)
		elif item_name in self.items:
			self.items[item_name] += quantity
			self.total += (quantity * price)
			print ("{} {} added to cart".format(quantity, item_name))
			print (self.items)
			return "Total amount: {}".format(self.total)

	def remove_item(self, item_name, quantity, price):
		if item_name in self.items and self.items[item_name] <= quantity:
			self.total -= (self.items[item_name] * price)
			del self.items[item_name]
			print ("{} removed from cart".format(item_name))
			print (self.items)
			return "Total amount: {}".format(self.total)
		elif item_name in self.items and self.items[item_name] > quantity:
			self.items[item_name] -= quantity
			self.total -= (quantity * price)
			print ("{} {} removed from cart: ".format(quantity, item_name))
			print (self.items)
			return "Total amount: {}".format(self.total)
		else:
			print ("Item not in cart")
			return "Total amount: {}".format(self.total)

	def checkout(self, cash_paid):
		if cash_paid >= self.total:
			cash_paid -= self.total
			return "Balance:", cash_paid
		else:
			return "cash_paid not enough"

class Shop(ShoppingCart):
	def __init__(self, quantity = 100):
		self.quantity = quantity

	def remove_item(self):
		self.quantity -= 1
		return "Quantity:", self.quantity

cart = ShoppingCart()
cart.add_item('mango', 2, 20)
cart.add_item('banana', 3, 30)
cart.remove_item('banana', 1, 30)
print (cart.total)
print(cart.checkout(130))











