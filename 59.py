source=raw_input("enter source")
dest=raw_input("enter destination")
with open(source) as f:
    with open(dest, "w") as f1:
        for line in f:
            f1.write(line)
