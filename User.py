
class User:
    def __init__(self, id, fname, lname, email, accType):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email = email
        self.accType = accType
        self.cart = []

    def editOnhand(self):
        while True:
            try:
                newQuantity = int(input('Enter quantity: '))
            except ValueError:
                print("Invalid value entered")
                continue
            if newQuantity < -self.quantity:
                print("Value cannot be greater than quantity")
                continue
            else:
                self.quantity += newQuantity
                break

    def viewAccType(self):
        return self.accType

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

    def getEmail(self):
        return self.email

    def getID(self):
        return self.id

    def viewCart(self):
        return self.cart

    def userInfo(self):
        return '{} {} {} {}'.format(self.id, self.fname, self.lname, self.email)