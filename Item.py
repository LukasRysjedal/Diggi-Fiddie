
class Item:
    def __init__(self, id, name, img):
        self.id = id
        self.name = name
        self.img = img

    def __str__(self):
        return f"Id: {self.id} Produkt: {self.name}"
