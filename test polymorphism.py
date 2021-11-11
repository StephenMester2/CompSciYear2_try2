
class private_shit:
    def __init__(self,cia_documents):
        self.__cia_documents = cia_documents
    def validation(self,password):

        if (password == "mynamejeff"):
            self.__changedocuments()
        else:
            exit
    def __changedocuments(self):
        password = input("Enter documents:")
        self.__cia_documents = password
    def printme(self):
        print(self.__cia_documents)

document1 = private_shit("Trump is a hot mama")
document1.validation(input("Enter Password: "))
document1.printme()








