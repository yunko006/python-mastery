from pathlib import Path

path = Path("Data\portfolio.dat")
# 1.3

# permet de lire de maniere plus elegantes les datas du fichier et de les mettre chaque ligne dans une list commune.
lines = path.read_text().splitlines()
# return ['AA 100 32.20', 'IBM 50 91.10', 'CAT 150 83.44', 'MSFT 200 51.23', 'GE 95 40.37', 'MSFT 50 65.10', 'IBM 100 70.44']

total = 0
for line in lines:
    listt = line.split()  # .split() va split de base par les espaces
    total += float(listt[1]) * float(listt[2])

print(total)


# 1.4 (a)
def portfolio_cost(path: Path) -> int:
    lines = path.read_text().splitlines()
    total = 0
    for line in lines:
        listt = line.split()
        total += float(listt[1]) * float(listt[2])

    return total


print(portfolio_cost(path))


# 1.4 (b)
def portfolio_cost2(path: Path) -> int:
    lines = path.read_text().splitlines()
    total = 0
    for line in lines:
        fields = line.split()
        try:
            nshares = int(fields[1])
            price = float(fields[2])
            total += nshares * price

        except ValueError as Error:
            print(f"pas pu parse la ligne {line} ")
            print(Error)

    return total


path2 = Path("Data\portfolio3.dat")
print(portfolio_cost2(path2))
