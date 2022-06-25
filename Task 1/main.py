def summa_diagonal_left (mass):
    y=0
    x=0
    res = 0
    x1 = 0
    y1 = 0
    while y < len(mass):
        while x < len(mass[y]):
            masiv_str = mass[y]
            aliment_masiva = masiv_str[x]
            print(f"Элимент {y, x} равен {aliment_masiva}.")
            if x1 == x and y1 == y:
                print(aliment_masiva)
                res += aliment_masiva
                print(res)
                x1 += 1
                y1 += 1
            # if x == 1 and y == 1:
            #     print(aliment_masiva)
            #     res += aliment_masiva
            # if x == 2 and y == 2:
            #     print(aliment_masiva)
            #     res += aliment_masiva
            #     print(res)
            x += 1
        y += 1
        x = 0


def main():
    massiv = [[22, 10, 12],
              [0, -4, 17],
              [44, 99, 14]]
    # for y in range(0, len(massiv)):
    #     for x in range(0, len(massiv[y])):
    #         masiv_str = massiv[y]
    #         aliment_masiva = masiv_str[x]
    #         print(f"Элимент {y, x} равен {aliment_masiva}.")
    summa_diagonal_left(massiv)



if __name__ == '__main__':
    main()
