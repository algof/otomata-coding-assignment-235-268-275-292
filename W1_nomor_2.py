import re

def is_valid_expression(expr):

    if len(expr) == 0: # Jika ekspresi kosong, return False
        return False

    expr = expr.replace(" ", "")  # Menghilangkan spasi untuk memudahkan pengecekan

    # Mengecek apakah tanda kurung sudah seimbang
    if not is_balanced(expr): # Jika tanda kurung tidak seimbang, return False
        return False

    # Base case: jika expr hanya angka, return True
    if re.fullmatch(r"\d+", expr): # Jika hanya angka, return True
        return True

    # Jika persamaan diapit oleh tanda kurung dan persamaan di dalamnya balanced, cek apakah persamaan di dalamnya valid
    if expr[0] == '(' and expr[-1] == ')' and is_balanced(expr[1:-1]):
        return is_valid_expression(expr[1:-1])

    # Mencari operator utama dalam persamaan
    index = find_main_operator(expr)
    if index == -1:
        return False

    left = expr[:index] # Bagian kiri dari operator utama
    right = expr[index+1:] # Bagian kanan dari operator utama

    # Rekursif cek apakah kedua bagian valid (kiri dan kanan dari operator utama)
    return is_valid_expression(left) and is_valid_expression(right)

def is_balanced(expr): # Mengecek apakah tanda kurung sudah seimbang
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: # Jika stack kosong return False
                return False
            stack.pop()
    return len(stack) == 0 # Return apakah stack sudah kosong, jika kosong True, jika tidak False

def find_main_operator(expr):
    level = 0
    for i in range(len(expr)):
        if expr[i] == '(':
            level += 1
        elif expr[i] == ')':
            level -= 1
        elif expr[i] in "+-*/" and level == 0:
            return i  # Mengembalikan posisi operator di luar tanda kurung
    return -1  # Tidak ditemukan operator yang valid

exprInput = input("Masukkan ekspresi matematika: ").strip()
if(is_valid_expression(exprInput)):
    print("Valid")
else:
    print("Tidak Valid")