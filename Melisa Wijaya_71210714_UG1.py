def calculate(pilihan, angka1, angka2):
    pilihan1 = angka1 + angka2
    pilihan2 = angka1 - angka2
    pilihan3 = angka1 * angka2
    pilihan4 = angka1 / angka2
    if pilihan == 1:
        print(pilihan1)
    elif pilihan == 2:
        print(pilihan2)
    elif pilihan == 3:
        print(pilihan3)
    elif pilihan == 4:
        print(pilihan4)
        
pilihan = int(input("Masukkan Pilihan: "))
while pilihan != 'Q':
    angka1 = int(input("Angka Pertama: "))
    angka2 = int(input("Angka Kedua: "))
    calculate(pilihan, angka1, angka2)