from models.UserModel import User
from models.DatabaseModel import Database

class UserRepository:
    def __init__(self):
        self.db = Database()

    def getUsers(self):
        users = self.db.query("SELECT * FROM users", fetchall=True)

        listUsers = []

        for user in users:
            listUsers.append(User(id=user[0],name=user[1], cpf=user[2], age=user[3]))

        return listUsers

    def getUserById(self, userId):
        user = self.db.query("SELECT * FROM users WHERE id = %s", (userId,))

        if user:
            user = User(id=user[0],name=user[1], cpf=user[2], age=user[3])
            return user
        return None

    def createUser(self, user):
        newUser = self.db.query("INSERT INTO users (name, cpf, age) VALUES (%s, %s, %s) RETURNING *", (user.name, user.cpf, user.age))

        newUser = User(id=newUser[0],name=newUser[1], cpf=newUser[2], age=newUser[3])

        return newUser

    def updateUser(self, userId, userData):
        updatedUser = self.db.query("UPDATE users SET name = %s, cpf = %s, age = %s WHERE id = %s RETURNING *", (userData.name, userData.cpf, userData.age, userId))
        
        updatedUser = User(id=updatedUser[0],name=updatedUser[1], cpf=updatedUser[2], age=updatedUser[3])
        return updatedUser

    def deleteUser(self, userId):
        self.db.execute("DELETE FROM users WHERE id = %s", (userId,))
        return True
    
    def getUserByCpf(self, cpf):
        user = self.db.query("SELECT * FROM users WHERE cpf = %s", (cpf,))

        if user:
            user = User(id=user[0],name=user[1], cpf=user[2], age=user[3])
            return user
        return None
