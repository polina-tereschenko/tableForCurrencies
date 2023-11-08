with open("README.md", "r") as file:
    lines = file.readlines()

with open("README.md", "w") as file:
    in_block = False
    for line in lines:
        if line.strip() == "## Supported Currencies":
            in_block = True
        if not in_block:
            file.write(line)
        if line.strip() == "## References":
            in_block = False
