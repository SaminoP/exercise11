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

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

if __name__ == "__main__":
    main()

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]