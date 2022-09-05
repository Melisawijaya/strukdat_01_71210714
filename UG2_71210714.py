import timeit

def fibonacci_iteratif(n):
    bil1 = 0
    bil2 = 1
    bil_selanjutnya = bil1 + bil2
    for i in range(n-2):
        bil1 = bil2
        bil2 = bil_selanjutnya
        bil_selanjutnya = bil1 + bil2
        
def fibonacci_rekursif(n):
    if n == 0:
        return
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)
    
for i in range(1, 10+1):
    start1 = timeit.default_timer()
    fibonacci_iteratif(i)
    end1 = timeit.default_timer()
    
    start2 = timeit.default_timer()
    fibonacci_rekursif(i)
    end2 = timeit.default_timer()
    
    print("n =", i, ", iteratif", end1-start1, "detik, rekursif", end2-start2, "detik")