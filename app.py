from flask import Flask
from controllers.UserController import UserController

app = Flask(__name__)
userController = UserController()

app.route('/users', methods=['GET'])(userController.getUsers)
app.route('/users/<int:userId>', methods=['GET'])(userController.getUserById)
app.route('/users', methods=['POST'])(userController.createUser)
app.route('/users/<int:userId>', methods=['PUT'])(userController.updateUser)
app.route('/users/<int:userId>', methods=['DELETE'])(userController.deleteUser)

if __name__ == '__main__':
    app.run(debug=True)

