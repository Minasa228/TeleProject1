class User:
    def __init__(self, login, password, access):
        self.login = login
        self.password = password
        self.access = access

    def display_info(self):
        print(f"Name: {self.login} type: {self.password} company: {self.access}")