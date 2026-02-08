class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # Prikaz informacija o proizvodu
    def display_info(self):
        return f"Proizvod: {self.name}, Cena: {self.price:.2f}, Količina: {self.quantity}"
    
    # Metoda koja azurira kolicine proizvoda
    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Količina ne može biti negativna")
    
    def __str__(self):
        return self.display_info()
