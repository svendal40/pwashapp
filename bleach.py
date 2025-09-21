class Bleach:

    def __init__(self, percentage: int, price_per_gallon: float = 7.00):
        
        self.percentage = percentage
        self.price_per_gallon = price_per_gallon

    def get_percentage(self) -> int:
        return self.percentage
   
    def set_percentage(self, percentage: int) -> None:
        self.percentage

    def get_price_per_gallon(self) -> float:
        return self.price_per_gallon
    
    def set_price_per_gallon(self, price_per_gallon: float = 7.00) -> None:
        self.price_per_gallon