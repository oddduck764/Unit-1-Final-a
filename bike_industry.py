class Wheel(object):
	def __init__(self, weight, cost, model, wheel_1, wheel_2, wheel_3):
		self.weight = weight
		self.cost = cost
		self.model = model
		self.wheel_1 = wheel_1
		self.wheel_2 = wheel_2
		self.wheel_3 = wheel_3

class Frames(object):
	def __init__(self, type, weight, manufacture_cost):
		self.type = type
		self.weight = weight
		self.manufacture_cost = manufacture_cost

class Model(object):
	def __init__(self, wheels, frame, total_weight, total_cost, model_name, model_manufacturer):
		self.wheels = wheels
		self.frame = frame
		self.total_weight = total_weight
		self.total_cost = total_cost
		self.model_name = model_name
		self.model_manufacturer = model_manufacturer

class Manufacturer(object):
	def __init__(self, manufacturer_name, model_1, model_2, model_3, percent_over_cost):
		self.manufacturer_name = manufacturer_name
		self.model_1 = model_1
		self.model_2 = model_2
		self.model_3 = model_3
		self.percent_over_cost = percent_over_cost

class Shops(object):
	def __init__(self, inventory_man, percent_over_price, name, inventory, profit):
		self.inventory_man = inventory_man
		self.percent_over_price = percent_over_price
		self.name = name
		self.inventory = inventory
		self.profit = profit

				
class Customers(object):
	def __init__(self, cust_name, bike_purchase):
		self.cust_name = cust_name
		self.bike_purchase = bike_purchase

		