class Restaurant:
    def __init__ (self, name, cuisine, menu: dict):
     self.name = name
     self.cuisine = cuisine
     self.menu = menu

   

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu: dict, drive_thru = bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru
    
    
    def order(self, food, quantity):
        if food in self.menu:
            if self.menu[food]['quantity'] >= quantity:                     
                price = self.menu[food]['price']
                self.menu[food]['quantity'] -= quantity
                return price * quantity
            else:
                return("Requested quantity not available")
        else:
            return("Dish not available!")
               



menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available