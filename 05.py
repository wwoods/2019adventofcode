
import sys

def main():
    f = open(sys.argv[1]).read()

    oints = [int(i.strip()) for i in f.split(',') if i.strip()]

    # Init
    # Init is n == 12, v == 2
    init_input = []
    if True:
        init_input.append((12, 2))
    else:
        for v in range(100):
            for n in range(100):
                init_input.append((n, v))

    halt = False

    for n, v in init_input:
        p = 0
        p_mode = 0
        def get_parms(ilist):
            r = []
            pp = p_mode
            for i in ilist:
                if pp % 10 == 0:
                    r.append(ints[i])
                elif pp % 10 == 1:
                    r.append(i)
                else:
                    raise NotImplementedError(pp)
                pp //= 10
            return r
        ints = oints[:]
        #ints[1] = n
        #ints[2] = v
        while True:
            i = ints[p]

            p_mode = i // 100
            i = i % 100

            print(f'code @{p}: {i} / {p_mode}')
            print(f'data: {ints[p:p+6]}')

            if i == 99:
                break
            elif i == 1:
                a, b = get_parms(ints[p+1:][:2])
                t = ints[p+1:][2]
                ints[t] = a + b
                p += 4
            elif i == 2:
                a, b = get_parms(ints[p+1:][:2])
                t = ints[p+1:][2]
                ints[t] = a * b
                p += 4
            elif i == 3:
                a, = ints[p+1:][:1]
                p += 2

                j = int(input('Input needed: '))
                ints[a] = j
            elif i == 4:
                a, = ints[p+1:][:1]
                p += 2
                print(f'output {ints[a]}')
            elif i == 5:
                a, b = get_parms(ints[p+1:][:2])
                if a != 0:
                    p = b
                else:
                    p += 3
            elif i == 6:
                a, b = get_parms(ints[p+1:][:2])
                if a == 0:
                    p = b
                else:
                    p += 3
            elif i == 7:
                a, b = get_parms(ints[p+1:][:2])
                t = ints[p+1:][2]
                ints[t] = 1 if a < b else 0
                p += 4
            elif i == 8:
                a, b = get_parms(ints[p+1:][:2])
                t = ints[p+1:][2]
                ints[t] = 1 if a == b else 0
                p += 4
            else:
                raise NotImplementedError(f'{i} / {p}')

        if halt and ints[0] == 19690720:
            print(f'n {n} v {v}')
            return


if __name__ == '__main__':
    main()


