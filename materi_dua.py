# array atau list di mulai dari angka 0
# maka write itu adalah 0 dan watch itu 3
myhobby = ["write", "read", "playing game", "watch"]
new_myhobby = myhobby

# cara menampilkan array atau list

# bisa menulis myhobby[0] untuk spesifik
print(myhobby[0])

# bisa menggunakan perhitungan
print(myhobby[2 - 1])

# contoh memanipulasi data array atau list

new_myhobby[2] = "Biliard"
print(f"new_myhobby = {new_myhobby}")
print(f"myhobby = {myhobby}")

# cara menghitung panjang atau isi array list
print(len(myhobby))

# -1 itu adalah data terakhir jadi setiap di -1 dari akhir maju ke paling awal
print(myhobby[len(myhobby)-1])
print(myhobby[len(myhobby)-1 -1])


cave_shape_one = "[]"
cave_one = [cave_shape_one] * 4

empty_cave_one = cave_one
empty_cave_one[2] = ":p"

print(cave_one)
print(empty_cave_one)


cave_shape_two = "[]"
cave_two = [cave_shape_two] * 4

empty_cave_two = cave_two.copy()
empty_cave_two[2] = ":p"

print(cave_two)
print(empty_cave_two)