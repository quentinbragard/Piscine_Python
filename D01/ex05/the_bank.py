class Account(object):
    ID_COUNT = 0
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        self.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        count_o_za = 0
        count_d_za = 0
        count_o_niv = 0
        count_d_niv = 0
        if type(origin) != Account or type(dest) != Account:
            exit("One of the account involved in the transaction is not securised (Object is wrong)")
        if len(dir(origin)) % 2 == 0 or len(dir(dest)) %2 == 0:
            exit("One of the account involved in the transaction is not securised (even number of attributes)")
        for elem in dir(origin):
            if elem[0] == 'b':
                exit("One of the account involved in the transaction is not securised (one attribute starts with a b in origin)")
            if elem.startswith("zip") or elem.startswith("addr") :
                count_o_za +=1
            if elem == "name" or elem == "id" or elem == "value":
                count_o_niv +=1
        for elem in dir(dest):
            if elem[0] == 'b':
                exit("One of the account involved in the transaction is not securised (one attribute starts with a b in dest)")
            if elem.startswith("zip") or elem.startswith("addr") :
                count_d_za +=1
            if elem == "name" or elem == "id" or elem == "value":
                count_d_niv +=1
        if count_o_za == 0 or count_d_za == 0:
            exit("One of the account involved in the transaction is not securised (no zip or addr)")
        if count_o_niv == 0 or count_d_niv == 0:
            exit("One of the account involved in the transaction is not securised (no name, id or value)")

    def fix_account(self, account):
        count_za= 0
        count_niv = 0
        if type(account) != Account:
            return (False)
        if len(dir(account)) % 2 == 0:
            account.elem_to_fix = "fixed"
        for elem in dir(account):
            if elem[0] == 'b':
                elem[0] = 'a'
            if elem.startswith("zip") or elem.startswith("addr") :
                count_za +=1
            if elem == "name" or elem == "id" or elem == "value":
                count_niv +=1
        if count_za == 0 or count_niv == 0:
            account.zip_code = "to_fill"
        return (True)


test = Account("test", value=1000)
test1 = Account("test1", value=1000, zip_code=88000, addr=88000)
test2 = (0,1,2,3)
Ma_Banque = Bank()
Ma_Banque.add(test)
Ma_Banque.add(test1)
#Ma_Banque.transfer(test, test1, 0)
#Ma_Banque.fix_account(test)
for elem in Ma_Banque.account:
    print(elem.name)
print(dir(test))