system = "@ ELY > "

terms = {}  # {position: value}
d = None
a1 = None

def author_info():
    info = {
        "Author": "Wanvisa Phumam",
        "YouTube": "Just Myeed",
        "Telegram": "@JustMyeed",
        "GitHub": "https://github.com/JustMyeed"
    }
    print("-" * 40)
    for key, value in info.items():
        print(f"{key:<8}: {value}")
    print("-" * 40)

def input_terms():
    global terms
    terms = {}
    try:
        count = int(input(system + "How many terms are given?\n$ Enter your answer: "))
        for _ in range(count):
            pos = int(input(system + "Term position (n): "))
            val = int(input(f"{system}Value of a{pos}: "))
            terms[pos] = val
    except ValueError:
        print(system + "Invalid input. Please enter numbers.")
        input_terms()

def input_difference():
    global d
    try:
        d = int(input(system + "Enter the common difference (d): "))
    except ValueError:
        print(system + "Invalid input. Please enter a number.")
        input_difference()

def calculate_d_and_a1():
    global d, a1
    if len(terms) < 2:
        print(system + "Need at least two terms to calculate d.")
        return
    sorted_terms = sorted(terms.items())
    (n1, a_n1), (n2, a_n2) = sorted_terms[:2]
    d = (a_n2 - a_n1) // (n2 - n1)
    a1 = a_n1 - (n1 - 1) * d
    print(system + f"Calculated d = {d}, a1 = {a1}")

def backtrack_a1():
    global a1
    if len(terms) == 1 and d is not None:
        n, a_n = next(iter(terms.items()))
        a1 = a_n - (n - 1) * d
        print(system + f"Backtracked a1 = {a1}")
    else:
        print(system + "Cannot backtrack a1. Need one term and d.")

def find_term():
    global a1, d
    if a1 is None:
        print(system + "Missing a1. Cannot proceed.")
        return
    while True:
        n = input(system + "Enter term position to find (or 'exit'): ")
        if n.lower() == "exit":
            break
        try:
            n = int(n)
            a_n = a1 + (n - 1) * d
            print(system + f"a{n} = {a_n}")
        except ValueError:
            print(system + "Invalid input.")

def main():
    author_info()
    input_terms()

    tag = {
        "y": "Yes, d is given.",
        "n": "No, d is not given.",
    }
    print("-" * 40)
    for key, value in tag.items():
        print(f"[{key}] {value}")
    choice = input(system + "Is the common difference (d) given? ").lower()

    if choice == "y":
        input_difference()
        backtrack_a1()
    elif choice == "n":
        calculate_d_and_a1()
    else:
        print(system + "Invalid choice.")

    find_term()
    print(system + "Thanks for using the solver!")

if __name__ == "__main__":
    main()
