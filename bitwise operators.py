# B5.1: Bitwise Operators

p = 12
q = 10

print("p =", p, "Binary:", bin(p))
print("q =", q, "Binary:", bin(q))

print("\nBitwise Operations:")
print("p & q  =", p & q)
print("p | q  =", p | q)
print("p ^ q  =", p ^ q)
print("~p     =", ~p)
print("p << 2 =", p << 2)
print("p >> 2 =", p >> 2)

# Sample Output:
# p = 12 Binary: 0b1100
# q = 10 Binary: 0b1010
#
# Bitwise Operations:
# p & q  = 8
# p | q  = 14
# p ^ q  = 6
# ~p     = -13
# p << 2 = 48
# p >> 2 = 3