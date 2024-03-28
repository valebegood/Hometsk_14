class Product:
     def __init__(self, name, price , quantity ):
          self.name = name
          self.price = price
          self.quantity = quantity

class Book(Product):
     def __init__ (self,name, price, quantity, author):
        super().__init__(name,price,quantity)
        self.author = author

     def read(self):
          print((f'Book info:\n' 
                 f'Book name: {self.name},\n'
                 f'Book price: {self.price},\n'
                 f'Book quantity: {self.quantity},\n'
                 f'Book author: {self.author},'
               ) )        

Harry_Potter = Book("Harry Potter", "100.0 USD!","10000 Copies","J.K. Rowling")    
Harry_Potter.read()