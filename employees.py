class Employees:

    def init(self, name: str, phone_number: str, email: str, pay_rate: float):
      self.names = name
      self.phone_number = phone_number
      self.email = email
      self.pay_rate = pay_rate
      
    def get_pay_rate(self) -> float:
        return self.pay_rate
    def set_pay_rate(self, pay_rate: float) -> None:
       self.pay_rate

    def get_name(self) -> str:
       return self.name
    
    def set_name(self, name: str) -> None:
       self.name

    def get_phone_number(self) -> str:
       return self.phone_number
    
    def set_phone_number(self, phone_number) -> None:
       self.phone_number

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email
    
    
