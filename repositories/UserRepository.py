# repositories/user_repository.py
from models.UserModel import User

class UserRepository:
    def __init__(self):
        self.users = []

    def getUsers(self):
        return self.users

    def getUserById(self, userId):
        return next((user for user in self.users if user.id == userId), None)

    def createUser(self, user):
        user.id = len(self.users) + 1

        self.users.append(user)
        return user

    def updateUser(self, userId, userData):
        user = self.getUserById(userId)
        user.name = userData.name
        user.cpf = userData.cpf
        user.age = userData.age
        return user

    def deleteUser(self, userId):
        self.users = [user for user in self.users if user.id != userId]
        return True
    
    def getUserByCpf(self, cpf):
        return next((user for user in self.users if user.cpf == cpf), None)
