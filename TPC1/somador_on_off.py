import sys

def somador(line):
    on = True
    acc = 0
    reading_value = 0
    i = 0

    while i < len(line):
        if line[i] in '0123456789' and on:
            reading_value = reading_value * 10 + int(line[i])
        else:
            if reading_value > 0:
                acc += reading_value
                reading_value = 0
            if line[i] == '=':
                print(str(acc))
            elif line[i].lower() == 'o':
                if i is not len(line) - 1 and line[i + 1].lower() == 'n':
                    on = True
                    i += 1
                elif i is not len(line) - 2 and line[i + 1].lower() == 'f' and line[i + 2].lower() == 'f':
                    on = False
                    i += 2
        i += 1

    if reading_value > 0:
        acc += reading_value
        reading_value = 0

    print(f"Valor final do acumulador: {acc}")


if len(sys.argv) > 1:
    file = open(sys.argv[1], 'r')
    somador(file.read())
else:
    for line in sys.stdin:
        somador(line)