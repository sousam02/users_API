from flask import jsonify, request
from repositories.UserRepository import UserRepository
from models.UserModel import User

class UserController:
    def __init__(self):
        self.userRepository = UserRepository()
    
    def getUsers(self):
        users = self.userRepository.getUsers()
        
        return jsonify([{
            'user_id': user.id, 
            'name': user.name, 
            'cpf': user.cpf, 
            'age': user.age
        } for user in users])
         

    def getUserById(self, userId):
        user = self.userRepository.getUserById(userId)
        if user:
            return jsonify({
                'id': user.id,
                'name': user.name, 
                'cpf': user.cpf,
                'age': user.age
            })
        return jsonify({'error': 'User not found'}), 404

    def createUser(self):
        data = request.get_json()
        
        if not data['name'] or not data['cpf'] or not data['age']:
            return jsonify({'error': 'Name, cpf and age are required'}), 400
        
        userByCpf = self.userRepository.getUserByCpf(data['cpf'])
        if userByCpf:
            return jsonify({'error': 'This CPF is already in use'}), 400
        
        newUser = User(name = data['name'], cpf=data['cpf'], age=data['age'])

        user = self.userRepository.createUser(newUser)
        return jsonify({
            "id": user.id,
            "name": user.name,
            "cpf": user.cpf,
            "age": user.age
        }), 201

    def updateUser(self, userId):
        userExists = self.userRepository.getUserById(userId)
        if not userExists:
            return jsonify({'error': 'User not Found'}), 404
        
        data = request.get_json()
        if not data['name'] or not data['cpf'] or not data['age']:
            return jsonify({'error': 'Name, cpf and age are required'}), 400
        
        userByCpf = self.userRepository.getUserByCpf(data['cpf'])
        if userByCpf and userByCpf.id != userId:
            return jsonify({'error': 'This CPF is already in use'}), 400
        
        userData = User(name=data['name'], cpf=data['cpf'], age=data['age'])

        updatedUser = self.userRepository.updateUser(userId, userData)
        return jsonify({
            'id': updatedUser.id,
            'name': updatedUser.name,
            'cpf': updatedUser.cpf,
            'age': updatedUser.age
        })


    def deleteUser(self, userId):
        userExists = self.userRepository.getUserById(userId)
        if not userExists:
            return jsonify({'error': 'User not Found'}), 404

        self.userRepository.deleteUser(userId)

        return jsonify(), 204

