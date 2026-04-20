from sorting import random_numbers
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        x = self.scores[index]

        if x >= 90:
            return "A"
        elif x >= 80:
            return "B"
        elif x >= 70:
            return "C"
        elif x >= 60:
            return "D"
        elif x >= 50:
            return "E"
        else:
            return "F"

    def find(self, target):
        found_indices = []

        for i in range(len(self.scores)):
            if self.scores[i] == target:
                found_indices.append(i)
        return found_indices

    def get_sorted(self):

        scores = self.scores.copy()
        x = len(scores)

        for i in range(x):
            for y in range(0, x - i - 1):

                if scores[y] > scores[y + 1]:
                    scores[y], scores[y + 1] = scores[y + 1], scores[y]
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print("def get_grade:\n")

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print("def find:\n")

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print("def get_sorted:\n")

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    print("overnie StudentsGrades:\n")
    print(results.count())
    for i in range(results.count()):
        p = results.get_by_index(i)
        g = results.get_grade(i)
        print(f"Student {i}: {p} points - {g}")
    print(results.find(100))
    print(results.get_sorted())
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())




if __name__ == "__main__":
    main()
print("skuska prvotnej funkcie:")
results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]