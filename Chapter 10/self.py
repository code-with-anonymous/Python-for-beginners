class Employee:
    name="Rayyan"
    language="python"
    stack="mern"
    def getPrint(self):
        print(f"The language is {self.language}")

harry=Employee()
harry.getPrint()    
harry.name="harry" #this is instance , has more pirorities
    
print(harry.language, harry.name,harry.stack )