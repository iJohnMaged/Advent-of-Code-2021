def read_file_lines(filename):
    with open(filename, "r") as file:
        return file.readlines()


sample_input = [int(x.strip()) for x in read_file_lines("puzzle.txt")]
a = sample_input[0]
b = sample_input[1]
c = sample_input[2]

answer = 0

for i in range(3, len(sample_input)):
    d = sample_input[i]
    if a + b + c < b + c + d:
        answer += 1
    a = b
    b = c
    c = d

print(answer)