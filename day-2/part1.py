horizontal_pos = 0
depth = 0

with open("puzzle.txt", "r") as f:
    for line in f.readlines():
        cmd, x = line.split()
        if cmd == "forward":
            horizontal_pos += int(x)
        elif cmd == "up":
            depth -= int(x)
        elif cmd == "down":
            depth += int(x)
        else:
            raise ValueError("Unknown Command")

print(f"Answer: {horizontal_pos * depth}")