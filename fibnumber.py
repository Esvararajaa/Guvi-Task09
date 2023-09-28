
# fibonacci series using lambda (recursive function)
f = lambda x: x if x <= 1 else f(x - 1) + f(x - 2)
# Ranging the element till 50
for i in range(50):
    # printing the each element
    print(f(i))
