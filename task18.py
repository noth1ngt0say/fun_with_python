f = open("text.txt", "w+t")
f.write("Hello\n")
f.seek(0)
print(f.read())
f.close()