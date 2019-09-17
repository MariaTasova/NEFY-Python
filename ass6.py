def get_largest_perimeter(L):
     L_sorted = sorted(L, reverse = True)
     a = L_sorted[0]
     b = L_sorted[1]
     c = L_sorted[2]
     if b+c > a:
         perimeter = a + b + c
         return(a, b, c, "perimeter=", perimeter)
     else:
         for i in range(3, len(L_sorted)):
             a = b
             b = c
             c = L_sorted[i]
             if b + c > a:
                perimeter = a + b + c
                return(a, b, c, "perimeter=", perimeter)

L = [2, 3,1,2,4, 6, 12, 1]
print(get_largest_perimeter(L))
