def factorial(n):
    """
    Oblicza silnię liczby n (n!).
    """
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Oblicza silnię (n!) dla podanej liczby n."
    )
    parser.add_argument("n", type=int, help="Liczba całkowita nieujemna")
    args = parser.parse_args()
    print(factorial(args.n))
