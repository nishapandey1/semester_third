#inheritance

#creation of parent class
class person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    
    def info(self):
        print("My name is", self.name)
        print("I am from", self.address)

parent_obj=person("pinky","KTM")
# parent_obj.info()


#creation of child class

class employee(person):
        
    def post(self):
        print("I am ethical hacker")

child_obj=employee("pinku","jhapa")
child_obj.info()
child_obj.post()
