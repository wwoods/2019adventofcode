
import sys
import torch

def main():
    f = open(sys.argv[1]).read()

    wa, wb = f.strip().split('\n')

    dirs = ['R', 'D', 'L', 'U']

    wa = wa.split(',')
    wb = wb.split(',')

    c = 20000
    a = torch.zeros(2 * c + 1, 2 * c + 1, dtype=torch.float)
    b = a.clone()

    for w, g in [(wa, a), (wb, b)]:
        x = c
        y = c

        sslick = 0
        print('WIRE')
        for ww in w:
            d = int(ww[1:])
            print(f'{x}, {y} -> {ww}')
            slick = sslick + 1 + torch.arange(d)
            sslick += d
            if ww[0] == 'R':
                g[x+1:x+d+1, y] = slick
                x += d
            elif ww[0] == 'D':
                g[x, y+1:y+d+1] = slick
                y += d
            elif ww[0] == 'L':
                slick = torch.tensor(list(slick)[::-1])
                g[x-d:x, y] = slick
                x -= d
            elif ww[0] == 'U':
                slick = torch.tensor(list(slick)[::-1])
                g[x, y-d:y] = slick
                y -= d
            else:
                raise NotImplementedError(ww)

    print("DONE")
    print(a)
    colls = (a * b).nonzero()
    if True:
        # Part 2
        for c in colls:
            apt = a[c[0], c[1]]
            bpt = b[c[0], c[1]]
            print(apt)
            print(bpt)
            print(f'{c[0]}, {c[1]}: {apt + bpt}')

        #a[colls] + b[colls])
    else:
        print('c')
        print(colls)
        colls -= torch.tensor([c, c]).view(-1, 2)
        print(colls)
        md = colls[:, 0].abs() + colls[:, 1].abs()
        print(md)
        md[md == 0] = 9999
        print(md.min())


if __name__ == '__main__':
    main()


