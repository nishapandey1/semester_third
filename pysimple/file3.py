# class student:
#     print ("hello")

# obj=student()

class student:
    def __init__(self,name,address,role):
        self.name=name
        self.address=address
        self.role=role

obj1=student("jubi","Ramechhap","student")


print("My name is {}". format(obj1.name))
print("I am from {}". format(obj1.address))
print("I am {}". format(obj1.role))


class teacher:
    def __init__(self,name,address,role):
        self.name=name
        self.address=address
        self.role=role

obj2=teacher("Ruby","Kathmandu","teacher")

print("My name is {}". format(obj2.name))
print("I am from {}". format(obj2.address))
print("I am {}". format(obj2.role))
