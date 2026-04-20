import random

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