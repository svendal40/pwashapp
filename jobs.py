import Bleach
import Employee
import Client


class Jobs:

    def __init__(self, type: str, levels: int, hard_sqft: float, soft_surfaces: int, siding: str, 
                 roofing: str, notes: str, bleach: int, client: Client, 
                 employees: list, untreated_wood: bool):
       
        self.customer_total_price = 0
        self.company_costs = 0
        
        self.type = type
        self.levels = levels
        self.hard_sqft = hard_sqft
        self.soft_surfaces = soft_surfaces
        self.siding = siding
        self.roofing = roofing
        self.notes = notes
        self.bleach = bleach
        self.client = client
        self.employees = employees
        self.untreated_wood = untreated_wood
        
        
    def customer_pricing(self,):
        
        hard_wash_price = 0.5 * self.hard_sqft
        soft_wash_price = 80 * self.soft_surfaces
        
        if self.untreated_wood:
            untreated_wood_price = int(input("enter notes about untreated wood and price")) 
            
            return hard_wash_price + soft_wash_price + untreated_wood_price
       
        return hard_wash_price + soft_wash_price 
    
    def company_costs(self) -> float:
        labor_costs = self.bleach.get_percentage() * self.bleach.get_price_per_gallon()

        for worker in self.employees:
            labor_costs += (worker.get_pay_rate() * self.worker_hours[worker])

        return labor_costs
             
        
    

        



        

