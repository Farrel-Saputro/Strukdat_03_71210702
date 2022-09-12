# input
input_kalimat = input("Masukan kalimat yang diinginkan\t: ")
input_kata = input("Masukan kata yang diinginkan\t: ")

# lower dan split
kalimat = input_kalimat.lower().split()
kata = input_kata.lower()

# proses
jumlah = 0
for i in kalimat:
    if i == kata:
        jumlah += 1

# output
print(jumlah)
