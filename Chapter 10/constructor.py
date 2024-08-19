class Employee:
    name="Rayyan"
    language="python"
    stack="mern"
    def __init__(self,name,language,salary):# dunder method which is automatically called

        self.name=name
        self.language=language
        self.salary=salary
        
    def getPrint(self):
        print(f"The language is {self.language}")
    @staticmethod
    def greet():
        print("Good morning")
    

harry=Employee("ahsan","javascript",1200000)
print(harry.name, harry.salary, harry.language)






# harry.getPrint()    
# harry.name="harry" #this is instance , has more pirorities
    
# print(harry.language, harry.name,harry.stack )