
import sys

def main():
    f = open(sys.argv[1]).read()

    oints = [int(i.strip()) for i in f.split(',') if i.strip()]

    # Init
    # Init is n == 12, v == 2
    for v in range(100):
        for n in range(100):

            p = 0
            ints = oints[:]
            ints[1] = n
            ints[2] = v
            while True:
                i = ints[p]
                if i == 99:
                    break
                elif i == 1:
                    a, b, t, *_ = ints[p+1:]
                    ints[t] = ints[a] + ints[b]
                    p += 4
                elif i == 2:
                    a, b, t, *_ = ints[p+1:]
                    ints[t] = ints[a] * ints[b]
                    p += 4
                else:
                    ints[0] = 0
                    break
                    raise NotImplementedError(f'{i} / {p}')

            if ints[0] == 19690720:
                print(f'n {n} v {v}')
                return


if __name__ == '__main__':
    main()


