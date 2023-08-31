"""
#Strip metodu kullanimi (fonksiyon)
def stripInput(myInput):
    myInput = myInput.strip("*") # Baştaki ve sondaki bütün "*" lari siler.
    print("Strip metodu kullanildi:",myInput)

#Replace metodu kullanimi (fonksiyon)
def replaceInput(myInput):
    myInput = myInput.replace(","," ") # "," leri " " ile değiştirir.
    newInput = myInput
    print("Replace metodu kullanildi:",myInput)

    return newInput

#lower() metodu kullanimi (fonskiyon)
def InputtoLower(myInput):
    myInput = myInput.lower()
    newinput = myInput
    print("Lower metodu kullanildi:",myInput)

    return newinput

#upper() metodu kullanimi (fonksiyon)
def InputtoUpper(myInput):
    myInput = myInput.upper()
    newinput = myInput
    print("Upper metodu kullanildi: ",myInput)

    return newinput

#kullanicidan input al
userInput = input("Enter an input: ")

#sorgular
if(type(userInput) == str and len(userInput) >= 10 ):
    newInput = InputtoUpper(userInput)
else:
    newInput = InputtoLower(userInput)

if(newInput.isupper() == True): # isupper(), Stringin upper durumunda olup olmadiğini kontrol eder.
    newInput = replaceInput(newInput)

stripInput(newInput)

"""

####################################################################

"""
#Veri Yapilari 1 - Listeler

# Liste metodlari "append() , remove() , insert() , pop()" 

newList = [1,2,3,4,5]

newList.append(6)

print("Sona eleman eklendi: ",newList)

newList.remove(2)

print("Istenilen eleman cikarildi: ",newList)

newList.insert(5,70)

print("Istenilen yere eleman eklendi: ",newList)

newList.pop()

print("Sondan eleman cikarildi: ",newList)

newList.pop(1)

print("Istenilen yerden eleman cikarildi: ",newList)

# Diğer liste metodlari

print("Listedeki bütün '5' ler sayildi: " , newList.count(5))
print("Listedeki '6' elemaninin indexine erisildi: ",newList.index(6))

newList2 = newList.copy()
print("Liste 'newList2' olarak kopyalandi ve newList2 yazdirildi: ",newList2)

newList2.extend(newList)
print("liste ile newList2 birleştirildi: ",newList2)

newList2.extend([1,2,3])
print("newList2 ye '[1,2,3]' eklendi: ",newList2)

newList2.reverse()
print("newList2 ters çevrildi: ",newList2)

newList3 = [4,2,5,1,3]
newList3.sort()
print("newList3 olusturulup '[4,2,5,1,3]' siralandi: ",newList3)

newList3.clear()
print("newList3 temizlendi:",newList3)

"""
#############################################################################
"""

#Veri Yapilari 2 - Tupleler

#Tuple olusturmak
#Tuple; elemanlari degistirilemeyen listedir.Atama islemi yapilamaz.

my_Tupple = (1,2,"emre",[4,5,6])

"""
#############################################################################

""" 

#Veri Yapilari 3 - Dictionary ler

#Dictionary Olusturmak
#Dictionary lerde indexleme ile eleman secilemez. my_Dictionary[0] gibi...

my_Dictionary = {"Emre" : 10,
                 "Asya" : [10,20],
                 "Oytun" : ["Nuray",20]}

print("my_Dictionary:",my_Dictionary)
print("my_Dictionary['Asya']: ",my_Dictionary["Asya"]) #Dictionaryden eleman secildi.

my_Dictionary["Emre"] = [10,30] #Eleman degistirildi.
print("['Emre'] degistirildi:",my_Dictionary)

my_Dictionary["Bahar"] = (70,90)
print("['Bahar'] eklendi",my_Dictionary)
 """
###########################################################################

""" 

#Veri Yapilari 4 - Setler

#Set Olusturmak
#Tekrar eden elemanlari ayirir,unique leştirir

my_Set = set()
sentence = "Ben bir gun yazilimci olacagim"

my_Set = set(sentence)
print(my_Set) # cikti: {'b', 'y', 'g', 'u', 'o', 'e', 'l', 'c', 'r', 'B', 'z', 'm', 'n', ' ', 'a', 'i'}

randomList = ["Ben" , "Ben" , "bir" ,"gün" , "yazilimci" , "yazilimci" , "olacagim"]
my_Set = set(randomList)

print(my_Set) #cikti {'Ben', 'gün', 'olacagim', 'bir', 'yazilimci'}

my_Set.add("2023'te")
print("Set'e eleman eklendi: ",my_Set)

my_Set.remove("2023'te") #eleman bulunamazsa hata verir
print("Set'ten eleman cikarildi:",my_Set)

my_Set.discard("bir") #eleman bulunamazsa hata vermez
print("Set'ten eleman cikarildi discard() ile: ",my_Set)

new_Set = set([1,2,3])
new_Set2 = set([1,3,5])

print("new_Set te olup new_Set2 de olmayan elemanlar:",new_Set.difference(new_Set2)) # difference() or (set1 - set2)
print("difference() metodunu iki sete de ayrı ayrı uygular:",new_Set.symmetric_difference(new_Set2)) # symmetric_difference()
print("Iki kumenin kesisimi alindi:",new_Set.intersection(new_Set2)) # intersection() or (set1 & set2)
print("Iki kumenin birlesimi alindi: ",new_Set.union(new_Set2)) # union()

#Eger uygulanan islem Set e aktarilmak istenirse

new_Set.intersection_update(new_Set2)
print("Iki setin kesisimini alip ilk sete atar: ",new_Set)
new_Set.difference_update(new_Set2)
print("Iki kumenin farkini alip ilk sete atar: ", new_Set)

#Setlerde sorgu Islemleri

new_Set = set([1,2,3,4,5,6,7])
new_Set2 = set([1,3,5,7])

print("Iki kumenin kesisimi bos mu:",new_Set.isdisjoint(new_Set2)) # isdisjoint()
print("Set1 Set2 nin alt kumesi mi: ",new_Set.issubset(new_Set2)) # issubset()
print("Set1 Set2 yi kapsiyor mu:",new_Set.issuperset(new_Set2)) # issuperset() """

##################################################################

""" #Funcitons

#Tek argumanli fonksiyon
def Squareof(x):
    print(x**2)

Squareof(2)

#Iki argumanli fonksyion
def XtimesY(x,y):
    print(x*y)

XtimesY(2,3) # Tek deger girilmesi hataya yol acar.

#On tanimli Arguman
def AtimesB(x,y=1):
    print(x*y)

AtimesB(3) #Tek deger girilmesi hataya yol acmaz.

#Deger donduren fonksiyon (return)
def XminusY(x,y = 0):
    return x-y

value = XminusY(4,1) #Deger value ye esitlendi
print(value) """


#############################################################

# if elif else Kullanimlari

#if ve else Kullanimi
""" carPrice = 100000
wallet = 120000

if(wallet >= carPrice):
    print("You bought the car.")

else:
    print("You couldn't buy the car.")

a = 1
b = 2


# elif Kullanimi
if(a>b):
    print("a > b")

elif(a<b):
    print("a < b")

else:
    print("a = b") """

###########################################################



