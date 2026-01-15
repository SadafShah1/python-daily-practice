class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

    def delete_user(self, user):
        print(f"{self.username} deleted user {user}")

admin = Admin("admin01", "admin@mail.com", "Super Admin")
