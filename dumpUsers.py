import json
from model.client import Client

if __name__ == "__main__":
    
    userDirectory = "projeto4-atm\\database\\users.json"

    with open(userDirectory) as fp:
        usersList = json.load(fp)

    user1 = Client("Gustavo Costa", "06646639159", "1234", "1710", 1000)
    user1Converted = vars(user1)
    
    user2 = Client("Clara Maíra", "124452234567", "123456", "0609", 2000)
    user2Converted = vars(user2)

    user3 = Client("Peter Parker", "12345678910", "78910", "1234", 1000)
    user3Converted = vars(user3)

    user4 = Client("Tony Stark", "10987654321", "111213", "6789", 2000)
    user4Converted = vars(user4)

    usersList.append(user1Converted)
    usersList.append(user2Converted)
    usersList.append(user3Converted)
    usersList.append(user4Converted)

    

    for user in usersList:
        print(f"{user}\n")

    with open(userDirectory, 'w') as updateFile:
        json.dump(usersList, updateFile, indent= 4)