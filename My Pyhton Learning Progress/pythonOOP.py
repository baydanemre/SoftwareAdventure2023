#PYTHON OBJECT ORIENTED PROGRAMMING (NESNE YONELIMLI PROGRAMLAMA)

#Basic Class
class Character():
    health = 100
    shield = 50
    power = 30
    Skills = []

""" print(Character.health)
Character.health = 200
print(Character.health)
 """
#Instantiation (Sınıf Orneklendirmesi)

""" reyna = Character()

print(reyna.health)
reyna.health = 300 # yeni değer atandı
print(reyna.health)

reyna.Skills.append("Blind") # yeni değer atandı
print(reyna.Skills)

print(Character.health) # Ön tanımlı olduğu için değişmedi
print(Character.Skills) # reynada yapılan değişiklik ana class ı etkiledi

    
sage = Character()
print(sage.Skills) # reynada yapılan değişiklik sonradan türetilen nesneleri etkiledi """

# __init__ ve self kullanimi Ornek Ozellikleri

""" class Employee():
    
    def __init__(self) -> None:
        self.department = ''
        self.surname = ''
        self.age = 0
        self.knownLanguages = []

emre = Employee()
emre.department = "computer science"
emre.knownLanguages.append("English")
print(emre.department,emre.knownLanguages)

asya = Employee()
asya.department = "Business"
asya.knownLanguages.append("Turkish")
print(asya.department,asya.knownLanguages) """

#Class icine fonksiyon eklemek

""" class Employee():
    
    def __init__(self) -> None:
        self.department = ''
        self.surname = ''
        self.age = 0
        self.knownLanguages = []

    def addLanguage(self,language):
        self.knownLanguages.append(language)

emre = Employee()
emre.addLanguage("English")
print(emre.knownLanguages) """

#Miras Yapilari (Inheritance)

""" class Employee():
    
    def __init__(self) -> None:
        self.surname = ''
        self.age = 0
    
class Business(Employee):

    def __init__(self) -> None:
        super().__init__()
        self.experience = ""

asya = Business()
asya.experience = "8"

emre = Business()
emre.experience = "7"

print(asya.experience , emre.experience)

class ComputerScience(Employee):
    def __init__(self,knownlanguages) -> None:
        super().__init__()
        self.knownlanguages = [knownlanguages]

    def addLanguage(self,language):
        self.knownlanguages.append(language)

oytun = ComputerScience("Python")
print(oytun.knownlanguages)

oytun.addLanguage("R")
print(oytun.knownlanguages)

selenay = ComputerScience("Java")
print(selenay.knownlanguages) """
