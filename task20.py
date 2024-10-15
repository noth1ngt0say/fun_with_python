# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные:
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

text_data = ["Beautiful is better than ugly", "Beautiful is better than ugly",
             "Simple is better than complex.", "Complex is better than complicated."]

def write_file():
    global text_data
    f = open("import_this.txt", "w+t", encoding="utf-8")
    for i in text_data:
        f.write(i + '\n')
    f.close()
def read_file():
    f = open("import_this.txt", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    return lines

write_file()
lines = read_file()
for line in lines[::-1]:
    print(line.strip())