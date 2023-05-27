from model.user import User

class Manager(User):

    def __init__(self, name, cpf, password, typeOfUser):
        super().__init__(name, cpf, password)
        self.typeOfUser = typeOfUser