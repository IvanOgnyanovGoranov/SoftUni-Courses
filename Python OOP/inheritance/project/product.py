class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, new_quantity: int) -> None:
        if self.quantity >= new_quantity:
            self.quantity -= new_quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity

    def __repr__(self) -> str:
        return self.name
