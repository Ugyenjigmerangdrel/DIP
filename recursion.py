def something(i):
    print(i)
    if i > 0:
        something(i-1)

something(10)