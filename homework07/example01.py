class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        result = ""
        for item in self.my_list:
            result += "\n"
            for inner_item in item:
                result += str(inner_item) + " "
        return result

    def __add__(self, other):
        summary = []
        final_summary = []
        for i in range(len(self.my_list)):
            summary = []
            for j in range(len(self.my_list[i])):
                summary.append(self.my_list[i][j] + other.my_list[i][j])
            final_summary.append(summary.copy())
        return Matrix(final_summary)


new_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
my_matrix = Matrix(new_list)

other_list = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]
other_matrix = Matrix(other_list)

print(my_matrix)

print(my_matrix + other_matrix)
