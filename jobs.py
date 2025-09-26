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
        
    def get_company_costs(self) -> float:
        return self.company_costs
    
    def set_company_costs(self, company_costs: int) -> None:
         self.company_costs = company_costs

    def get_type(self) -> str:
        return self.type

    def set_type(self, type: str) -> None:
        self.type = type
    
    def get_levels(self) -> int:
        return self.levels

    def set_levels(self, levels: int) -> None:
        self.levels = levels

    def get_hard_sqft(self) -> float:
        return self.hard_sqft
    
    def set_hard_sqft(self, hard_sqft: float) -> None:
        self.hard_sqft = hard_sqft

    def get_soft_surfaces(self,) -> int:
        return self.soft_surfaces
    
    def set_soft_surfaces(self, soft_surfaces: int) -> None:
        self.soft_surfaces = soft_surfaces
    
    def get_siding(self) -> str:
        return self.siding
    
    def set_siding(self, siding: str) -> None:
        self.siding = siding

    def get_roofing(self) -> str:
        return self.roofing

    def set_roofing(self, roofing: str) -> None:
        self.roofing = roofing 

    def get_notes(self) -> str:
        return self.notes
    
    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def get_bleach(self) -> int:
        return self.bleach
    
    def set_bleach(self, bleach: int) -> None:
        self.bleach = bleach

    def get_client(self) -> str:
        return self.client
    
    def set_client(self, client: str) -> None:
        self.client = client

    def get_employees(self) -> list:
        return self.employees
    
    def set_employees(self, employees: list) -> None:
        self.employees = employees

    def get_untreated_wood(self) -> bool:
         return self.untreated_wood
    
    def set_untreated_wood(self, untreated_wood: bool) -> None:
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
             
        
    

        



        

