class Film:
    def __init__(self, title, type, company):
        self.title = title
        self.type = type
        self.company = company

    def display_info(self):
        print(f"Name: {self.title} type: {self.type} company: {self.company}")

