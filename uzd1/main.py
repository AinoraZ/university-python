import numpy as np
import sympy as sp


# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
def f1_interval():
    return np.linspace(-1.3, 2.5, 64)


# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
def f2_3n_array(n):
    return np.tile([1, 2, 3], 3 * n)


# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
def f3_odd_numbers():
    return np.fromfunction(lambda i: (i * 2) + 1, (10,), dtype=int)


# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
def f4_2d_zero_array_padded():
    arr = np.zeros((10, 10), dtype=int)
    arr = np.pad(arr, 1, mode="constant", constant_values=(1,))

    return arr


# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
def f5_chessboard():
    arr = np.zeros((8, 8), dtype=int)
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1

    return arr


# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
def f6_n_on_n_sum(n):
    return np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)


# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
def f7_random():
    arr = np.random.rand(3, 5)
    arr_sum = arr.sum()
    row_sum = arr.sum(axis=1)
    col_sum = arr.sum(axis=0)

    return {"sum": arr_sum, "row-sum": row_sum, "col-sum": col_sum, "arr": arr}


# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
def f8_random_sorted():
    arr = np.random.rand(5, 5)
    indices = np.argsort(arr[:, 1])
    return arr, arr[indices]


# 9. Atvirkštinę matricą
def f9_inverse():
    arr = np.array([[-3, 1], [5, 0]])
    return np.linalg.inv(arr)


# 10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
def f10_eigenvector():
    arr = np.array([[-3, 1], [5, 0]])
    return np.linalg.eig(arr)


# 11. Pasirinktos funkcijos išvestinę
def f11_diff():
    x = sp.Symbol('x')
    y = x**2 + 2*x + 1  # f(x^2 + 2x + 1)` =  2x + 2
    return y.diff(x)


# 12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
def f12_integral():
    x = sp.Symbol('x')
    a = sp.Symbol('a')
    b = sp.Symbol('b')
    y = 2*x + 2
    return sp.integrate(y, (x,)), sp.integrate(y, (x, a, b))


print(f1_interval().shape, f1_interval())
print(f2_3n_array(20).shape, f2_3n_array(20))
print(f3_odd_numbers().shape, f3_odd_numbers())
print(f4_2d_zero_array_padded().shape, f4_2d_zero_array_padded(), sep="\n")
print(f5_chessboard().shape, f5_chessboard(), sep="\n")
print(f6_n_on_n_sum(10).shape, f6_n_on_n_sum(10), sep="\n")

for key, value in f7_random().items():
    print(f"{key}:", value)

original_arr, sorted_arr = f8_random_sorted()
print(original_arr, sorted_arr, sep="\n")

print(f9_inverse())
print(f10_eigenvector())
print(f11_diff())
print(f12_integral())

