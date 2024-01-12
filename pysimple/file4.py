class student:
    def __init__(self,name,address,role):
        self.name=name
        self.address=address
        self.role=role
    
    def info1(self):
        print("My name is", self.name)
        print("I am from", self.address)
        print("I am", self.role)

class teacher:
    def __init__(self,name,address,role):
        self.name=name
        self.address=address
        self.role=role
    
    def info2(self):
        print("My name is", self.name)
        print("I am from", self.address)
        print("I am", self.role)

obj1=student("jubi","Ramechhap","student")
obj2=teacher("Ruby","Kathmandu","teacher")

obj1.info1()

obj2.info2()

