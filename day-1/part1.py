def read_file_lines(filename):
    with open(filename, "r") as file:
        return file.readlines()


sample_input = [int(x.strip()) for x in read_file_lines("puzzle.txt")]
answer = sum(
    [sample_input[i] < sample_input[i + 1] for i in range(len(sample_input) - 1)]
)
print(answer)