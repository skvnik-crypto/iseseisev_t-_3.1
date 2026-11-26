#12 "Heina niitmise brigaadis on N niidukit"
while True:
    try:
        N = int(input("Sisesta niidikuse kogus: "))
    except ValueError:
        print("Viga. Palun sisesta kehtiv täisarv")
    if N < 0:
        print("Viga. Palun sisesta positiivne täisarv")
    elif N == 0:
        print("Viga. Null ei ole võimalik")

    try:
        m = float(input("Sisesta niidikuse tööaeg: "))
    except ValueError:
        print("Viga. Palun sisesta kehtiv täisarv")
    if N < 0:
        print("Viga. Palun sisesta positiivne täisarv")
    elif N == 0:
        print("Viga. Null ei ole võimalik")
print("Aeg on m")



#15
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()