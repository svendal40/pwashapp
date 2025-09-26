class Client:

    def __init__(self, name: str, email: str, address: str, phone: str) -> None:

        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email = email

    def get_address(self) -> str:
        return self.address
    
    def set_address(self, address: str) -> None:
        self.address = adress

    def get_phone(self) -> str:
        return self.phone

    def set_phone(self, phone: str) -> None:
        self.phone = phone