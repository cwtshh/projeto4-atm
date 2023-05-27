class BalanceScreen:
    def __init__(self, user):
        print("#---------------------------------#")
        print(f"# Saldo de {user['name']}        ")
        print(f"# R$ {user['money']}")
        print("#                                 #")
        print("#---------------------------------#")