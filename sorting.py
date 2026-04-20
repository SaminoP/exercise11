import random
#import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    number = numbers.copy()
    n = len(number)

    for i in range(n):

        min = i

        for x in range(i + 1, n):
            if number[x] < number[min]:
                min = x

        number[i], number[min] = number[min], number[i]

    return number

def main():
    seznam = [5, 1, 4, 2, 8]
    y = random_numbers(20)

    zoradeny = selection_sort(seznam)

    print(f"povodny: {seznam}")
    print(f"zoradeny: {zoradeny}")

    zoradeny2 = selection_sort(y)

    print(f"povodny: {y}")
    print(f"zoradeny: {zoradeny2}")

if __name__ == "__main__":
    main()


def bubble_sort(zoznam):
    cisla = zoznam.copy()
    x = len(cisla)

    # plt.ion()
    # plt.show()

    for i in range(x):
        for y in range(0, x - i - 1):

            # index_highlight1 = y
            # index_highlight2 = y + 1
            #
            # colors = ["steelblue"] * len(cisla)
            # colors[index_highlight1] = "tomato"
            # colors[index_highlight2] = "tomato"
            #
            # plt.clf()  # Vymaže predchádzajúci snímok
            # plt.bar(range(len(cisla)), cisla, color=colors)
            # plt.title("Bubble Sort - Vizualizácia")
            # plt.pause(0.1)


            if cisla[y] > cisla[y + 1]:
                cisla[y], cisla[y + 1] = cisla[y + 1], cisla[y]

        # plt.ioff()
        # plt.show()

    return cisla



def main():
    seznam = [5, 1, 4, 2, 8]
    y = random_numbers(20)

    zoradeny = bubble_sort(seznam)

    print(f"povodny: {seznam}")
    print(f"zoradeny: {zoradeny}")

    zoradeny2 = bubble_sort(y)

    print(f"povodny: {y}")
    print(f"zoradeny: {zoradeny2}")

if __name__ == "__main__":
    main()