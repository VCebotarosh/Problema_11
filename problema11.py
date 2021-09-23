def afisare():
    print("\n")

def calcul_divizori(n):
    divizor=0
    for i in range(1,n+1):
        if(n%i==0):
            divizor+=1
    if divizor>=1 and divizor<=4:
        return n
    else:
        return None

nr_elemente=int(input("Dati numarul de elemente al vectorului "))
vector=[]
vector2=[]
vector5=[]
if (nr_elemente<10 and nr_elemente>0):
    for i in range(nr_elemente):
        vector.append(int(input(f"Elementul pe pozitia {i} este : ")))

print(vector)
print("Afisati elementele vectorului cu pasul 5" ,vector[::5])
print("Afisati elementele vectorului in ordinea inversa introducerii de la tastatura",vector[::-1])
vector1=vector.copy()
vector1.sort(reverse=True)
print("Afisati vectorul initial in ordinea descrescatoare",vector1)
print("Afiseaza la ecran doar elementele pare: ")
for element in vector:
    if element%2==0:
        print(element, end=' ')
        vector2.append(element)
afisare()
print(f"Media aritmetica a elementelor pare este {round(sum(vector2)/len(vector2),3)}")
print("Afiseaza pe ecran doar elementele impare: ")
for element in vector:
    if element%2!=0:
        print(element, end=' ')

afisare()
x=int(input("Dati valoarea lui x: "))
y=int(input("Dati valoarea lui y: "))
print(f"Elementele mai mare ca {x} si nu sunt divizibile cu {y} sunt: ")
for element in vector:
    if(element>x) and (element%y!=0):
        print(element, end=" ")
        
afisare()
print(f"Elementele care sunt mai mari decat {x} si mai mici ca {y} sunt: ")
for element in vector:
    if(element>x) and (element<y):
        print(element, end=" ")

afisare()
print(f"Afiseaza pe ecran pozitia(indicii) componentelor impare negative")
for element in vector:
    if (element<0) and (element%2!=0):
        element=vector.index(element)
        print(element, end=" ")
        
afisare()
print(f"Afiseaza pe ecran pozitia elementelor ce contin doar 2 cifre semnificative:")
for i  in range(len(vector)):
    if (vector[i]>9 and vector[i] <100) or (vector[i]>-100 and vector[i] <-9):
        print(i, end=" ")
afisare()
vector3=vector.copy()
vector3[0]=min(vector3)
print(f"Inlocueste prima componenta cu componenta de valoare minima: {vector3}")
vector4=vector.copy()
minim=vector4.index(min(vector4))
initial=vector4[0]
del(vector4[minim])
vector4.insert(minim, initial)
print(f"Vectorul in care minimul se schimba cu elementul primul este: {vector4}")
print(f"Vectorul nou creat cu elementele pare ale tabloului initial este {vector2}")
for element in vector:
    if element%3==0:
        vector5.append(element)
print(f"Vectorul care cuprinde doar elementele divizibile la 3 din cel initial este {vector5}")
vector6=list(filter(lambda x: x is not None, map(calcul_divizori,vector)))
print(f"Vectorul format doar din acele componente ale tabloului introuds de la tastatura care au cel mult patru divizori este: {vector6}")


