from multiprocessing import Pool

def add(x, y):
    """Return the sum of the tuple of two arguments"""
    return x+y

a_b = [(1,6), (2,7), (3,8), (4,9), (5,10)]

if __name__ == "__main__":
    with Pool() as pool:
        result = pool.starmap(add, a_b)

    print(result)


