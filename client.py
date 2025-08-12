class Client:

    def __init__(self, name: str, email: str, address: str, phone: str) -> None:

        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

    def get_name(self) -> str:
        return self.name