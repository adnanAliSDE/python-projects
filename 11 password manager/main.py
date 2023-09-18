'''Password Manager that helps user to:
1-View saved passwords 
2-Set new passwords
3-Update passwords
4-Passwords will be stored in encrypted form'''
secret_key=""
import encrypter as enc


class Manager:
    def __init__(self, provider, username, password):
        self.provider = provider
        self.username = username
        self.password = password

    def save(self):
        with open("data.csv", "a") as f:
            f.write(f"{self.provider},{self.username},{self.password}\n")
        print("Object saved successfully")

    def changePassword(self, index, newPassword):
        l = None
        with open("data.csv") as f:
            l = f.readlines()
            print(l[index])
            st = l[index]
            data = st.split(',')
            st = f"{data[0]},{data[1]},{enc.decrypt(newPassword)}\n"
            l[index] = st
            print(l[index])
        with open("data.csv", 'w') as f:
            f.writelines(l)
        print("Changed password successfully")
        print(f"New password: {newPassword}")

    def findPassword(self):
        data = f"{self.provider},{self.username}"
        i = None
        with open("data.csv") as f:
            lines = f.readlines()
            for index, line in enumerate(lines):
                if line.startswith(data):
                    data = line[:-1]
                    i = index
                    break

        password = data.split(",")[2]
        password = enc.decrypt(password)
        return password, i


m = None


def setAccount():
    provider = enc.encrypt(input("Enter Account provider: ").lower())
    username = enc.encrypt(input("Enter username: "))
    password = enc.encrypt(input("Enter password: "))
    m = Manager(provider, username, password)
    m.save()


def changePassword():
    provider = enc.encrypt(input("Enter account provider: "))
    username = enc.encrypt(input("Enter username: "))
    m = Manager(provider, username, None)
    index = m.findPassword()[1]
    newPassword = enc.encrypt(input("Enter new password: "))
    m.changePassword(index, newPassword)


def viewPassword():
    provider = enc.encrypt(input("Enter the provider name: ").lower())
    username = enc.encrypt(input("Enter username: "))
    m = Manager(provider, username, None)
    password = m.findPassword()[0]
    print(f"Your password: {password}")


options = ["Set new account", "Change Password", "View Password"]

for index, value in enumerate(options):
    print(f"{index}-{value}")
option = int(input("Please choose an option to proceed: "))

match option:
    case 0:
        setAccount()
    case 1:
        changePassword()
    case 2:
        viewPassword()
    case _:
        raise ValueError("Please provide a valid input")
