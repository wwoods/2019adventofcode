
import sys

def main():
    f = open(sys.argv[1]).read()
    fuel = 0
    fuelfuel = 0
    for line in f.split('\n'):
        line = line.strip()
        if not line: continue

        n = int(line)
        fuel += n // 3 - 2

        f = [n // 3 - 2]
        while True:
            ff = f[-1] // 3 - 2
            if ff <= 0:
                break
            f.append(ff)
        fuelfuel += sum(f)
    print('A')
    print(fuel)
    print('B')
    print(fuelfuel)


if __name__ == '__main__':
    main()


