def getPandasFile(filename):
    import pandas as pd
    # Hvis filen er adskilt af tabulatorer (\t):
    df = pd.read_csv(filename, sep="\t")

    # Hvis kolonnerne er adskilt af et vilkårligt antal mellemrum/tabulatorer:
    # df = pd.read_csv("filnavn.txt", sep=r'\s+')

    return df

def getRawFile(filename):
    data = []

    with open(filename, "r", encoding="utf-8") as fil:
      for linie in fil:
        # Fjerner linjeskift og splitter ved tabulator
        kolonner = linie.strip().split("\t")
        data.append(kolonner)

    # 'data' er nu en liste af lister (rækker og kolonner)
    return data
if __name__ == "__main__":
    myfile = getRawFile("employees.txt")
    print(myfile)
    myfile2 = getPandasFile("employees.txt")
    print(myfile2)