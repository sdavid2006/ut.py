# ut1 = int(input('Add meg az első út hosszát (km): '))
# ut2 = int(input('Add meg a második út hosszát (km): '))

# kilometerek = []
# kilometerek.append(ut1/1000)
# kilometerek.append(ut2/1000)

# if ut1 > ut2:
#     print(f'Az első út hossza nagyobb ({ut1}km)')
#     print(f'A második út hossza kisebb ({ut2}km)')
# elif ut1 == ut2:
#     print(f'A két út hossza egyenlő. ({ut1})')
# else:
#     print(f'Az első út hossza kisebb ({ut1}km)')
#     print(f'A második út hossza nagyobb ({ut2}km)')
# def méter(m):
#     if ut1 != "" and ut2 != "":
#         return(ut1*1000)
#         return(ut2*1000)
# def vizsgálat(vizs):
#     if kilometerek[0] < 200:
#         return(f'Az út rövid')
#     elif kilometerek[0] > 200 and kilometerek[0] < 500:
#         return(f'Az út közép hosszú')
#     elif kilometerek[0] > 500:
#         return(f'Az út hosszú')
#     else:
#         return('Hibás Adat!')


## ----------------------------------------
def mérföld(mi):
    if hosszak[i] != "":
        return(f'Mérföld: {hosszak[i]/1.609:0.2f}')
def vizsgálat(uthossz):
        if hosszak[i] < 200:
            return(f'Az út rövid ({hosszak[i]}km)')
        elif hosszak[i] > 200 and hosszak[i] < 500:
            return(f'Az út közép hosszú ({hosszak[i]}km)')
        elif hosszak[i] > 500:
            return(f'Az út hosszú ({hosszak[i]}km)')
        else:
            return('Hibás Adat!')
út = []
hosszak = []

for i in range(3):
    utszam = str(input('Add meg az út nevét: '))
    uthossz = float(input('Add meg az út hosszát (km) : '))
    út.append(utszam)
    hosszak.append(uthossz)
    print(f'{vizsgálat(uthossz)}')
    print(f'{mérföld(uthossz)}')
    print(f'{sum(hosszak)}')