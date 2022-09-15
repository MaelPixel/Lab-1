secondes=31536004
def annne(secondes):
    annees, secondes= divmod(secondes,31536000)
    print(annees)
    print(secondes)
annne(secondes)