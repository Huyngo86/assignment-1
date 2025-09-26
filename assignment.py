# ===== BÀI 1 =====
# A = {n : n^2 + 2n chia hết cho 15}
# B = {0..10000}
# C = {tích của 2 số nguyên tố khác nhau}

# ---------------------------
A = []
B = []
for n in range(0, 10001):
    B.append(n)
    if (n*n + 2*n) % 15 == 0:
        A.append(n)


# ---------------------------
# Ý 1: B \ A
B_tru_A = []
for x in B:
    if x not in A:
        B_tru_A.append(x)

print("Ý 1:", len(B_tru_A))


# ---------------------------
# Ý 2: 100-th phần tử của A ∩ B (giảm dần)
A_giao_B = []
for x in B:
    if x in A:
        A_giao_B.append(x)

A_giao_B.sort(reverse=True)
print("Ý 2: phần tử thứ 100 của A ∩ B (giảm dần) =", A_giao_B[99])




# ---------------------------
# Ý 3: Sinh tập C

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0: 
            return False 

    return True  
C = []
nguyen_to = []
for i in range(2, 10001):
    if la_so_nguyen_to(i):
        nguyen_to.append(i)

for i in range(len(nguyen_to)):
    for j in range(i+1, len(nguyen_to)):
        tich = nguyen_to[i] * nguyen_to[j]
        if tich <= 10000:
            C.append(tich)

C.sort()

print("Ý 3: phần tử thứ 100 =", C[99])


# ---------------------------
# Ý 4: B ∩ C
B_giao_C = []
for x in B:
    if x in C:
        B_giao_C.append(x)

print("Ý 4:", len(B_giao_C))
# Question 3: Solve the logic equation:
# (p ∨ q) → r = (p ⊕ r) ∧ q.
