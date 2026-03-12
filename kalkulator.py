#!/usr/bin/env python3
"""
Prosty kalkulator obsługujący podstawowe operacje arytmetyczne.

Użycie:
    python kalkulator.py add 2 3
    python kalkulator.py sub 5 2
    python kalkulator.py mul 4 6
    python kalkulator.py div 10 2

Można także uruchomić w trybie interaktywnym:
    python kalkulator.py
"""

import argparse
import sys

def add(a: float, b: float) -> float:
    """Zwraca sumę a i b."""
    return a + b

def sub(a: float, b: float) -> float:
    """Zwraca różnicę a - b."""
    return a - b

def mul(a: float, b: float) -> float:
    """Zwraca iloczyn a i b."""
    return a * b

def div(a: float, b: float) -> float:
    """Zwraca iloraz a / b. Rzuca ZeroDivisionError przy dzieleniu przez zero."""
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero jest niedozwolone.")
    return a / b

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Prosty kalkulator wiersza poleceń."
    )
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # Dodawanie
    parser_add = subparsers.add_parser("add", help="Dodaj dwie liczby.")
    parser_add.add_argument("a", type=float, help="Pierwsza liczba.")
    parser_add.add_argument("b", type=float, help="Druga liczba.")

    # Odejmowanie
    parser_sub = subparsers.add_parser("sub", help="Odejmij drugą liczbę od pierwszej.")
    parser_sub.add_argument("a", type=float, help="Minuend.")
    parser_sub.add_argument("b", type=float, help="Subtrahend.")

    # Mnożenie
    parser_mul = subparsers.add_parser("mul", help="Pomnóż dwie liczby.")
    parser_mul.add_argument("a", type=float, help="Pierwsza liczba.")
    parser_mul.add_argument("b", type=float, help="Druga liczba.")

    # Dzielenie
    parser_div = subparsers.add_parser("div", help="Podziel pierwszą liczbę przez drugą.")
    parser_div.add_argument("a", type=float, help="Licznik.")
    parser_div.add_argument("b", type=float, help="Mianownik.")

    return parser.parse_args(argv)

def main():
    # Jeśli skrypt uruchomiony bez argumentów, przejdź w tryb interaktywny
    if len(sys.argv) == 1:
        print("Tryb interaktywny. Wpisz 'exit' aby zakończyć.")
        while True:
            try:
                line = input(">>> ").strip()
                if line.lower() in ("exit", "quit"):
                    break
                if not line:
                    continue
                parts = line.split()
                args = parse_args(parts)
                result = execute(args)
                print(result)
            except Exception as e:
                print(f"Błąd: {e}")
        return

    args = parse_args()
    try:
        result = execute(args)
        print(result)
    except Exception as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)

def execute(args):
    """Wykonuje wybraną operację na podstawie sparsowanych argumentów."""
    ops = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
    }
    func = ops.get(args.operation)
    return func(args.a, args.b)

if __name__ == "__main__":
    main()
