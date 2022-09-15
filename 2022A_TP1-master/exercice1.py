def div3(n):
    if float(n)%3==0 and float(n)%5!=0:
        print("fizz")
        return
    else:
        return
def div5(n):
    if float(n)%5==0 and float(n)%3!=0:
        print("buzz")
        return
    else:
        return
def div3_5(n):
    if float(n)%5==0 and float(n)%3==0:
        print("fizzbuzz")
def ndiv3_5(n):
    if float(n)%5!=0 and float(n)%3!=0:
        print(n)

def fizzBuzz(n):
    div3(n)
    div5(n)
    div3_5(n)
    ndiv3_5(n)

    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.

    resultat = n
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    fizzBuzz(n)
