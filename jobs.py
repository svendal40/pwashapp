import Bleach
import Employee
import Client


class Jobs:

    def __init__(self, type: str, levels: int, sqft: float, siding: str, 
                 roofing: str, notes: str, bleach: Bleach, client: Client, 
                 employees: list):
        
        self.type = type
        self.levels = levels
        self.sqft = sqft
        self.siding = siding
        self.roofing = roofing
        self.notes = notes
        self.bleach = bleach
        self.client = client
        self.employees = employees

        
        
        

