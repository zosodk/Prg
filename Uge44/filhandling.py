def getPandasFile(filename):
    import pandas as pd
    # Hvis filen er adskilt af tabulatorer (\t):
    df = pd.read_csv(filename, sep="\t")

    # Hvis kolonnerne er adskilt af et vilkårligt antal mellemrum/tabulatorer:
    # df = pd.read_csv("filnavn.txt", sep=r'\s+')

    return df
def openFile(filename, mode="r"):
    return open(filename, mode, encoding="utf-8")

def createFileWrite(filename, data):
    with open(filename, "w", encoding="utf-8") as fil:
        fil.write(data)
    fil.close()

def createFileAppend(filename, data):
    with open(filename, "a", encoding="utf-8") as fil:
        fil.write(data)
    fil.close()

def getRawFile(filename):
    data = []

    with open(filename, "r", encoding="utf-8") as fil:
      for linie in fil:
        # Fjerner linjeskift og splitter ved tabulator
        kolonner = linie.strip().split("\t")
        data.append(kolonner)


    # 'data' er nu en liste af lister (rækker og kolonner)
    return data
def splitRawFileByColumns(filename):
    data = []
    fornavne = []
    efternavne = []
    uddannelse = []
    anciennitet = []
    with open(filename, "r", encoding="utf-8") as fil:
        placering = 0
        for linie in fil:
            person = linie.strip().split("\t")
            fornavne.append(person[0])
            efternavne.append(person[1])
            uddannelse.append(person[2])
            anciennitet.append(person[3])
            placering += 1
    #print(fornavne)
    data.append(fornavne)
    data.append(efternavne)
    data.append(uddannelse)
    data.append(anciennitet)
    return data
if __name__ == "__main__":
    #myfile = getRawFile("employees.txt")
    #print(myfile[0])

    #myfile2 = getPandasFile("employees.txt")
    #print(myfile2)
    dataindhold = splitRawFileByColumns("employees.txt")
    #print(dataindhold)
    for data in dataindhold:
        print(data)