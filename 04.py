
def main():
    i = '123257-647015'
    mn, mx = i.split('-')
    mn = int(mn)
    mx = int(mx)

    # Must have double, must be always increasing
    count = 0
    for i in range(mn, mx+1):
        s = str(i)
        dbl = set()
        seen = {}
        dec = False
        seen[s[0]] = seen.get(s[0], 0) + 1
        for j in range(1, len(s)):
            seen[s[j]] = seen.get(s[j], 0) + 1
            if s[j-1] == s[j]:
                dbl.add(s[j])
            if ord(s[j-1]) > ord(s[j]):
                dec = True
        if dbl and not dec:
            for d in dbl:
                if seen[d] == 2:
                    count += 1
                    break
    print(count)


if __name__ == '__main__':
    main()

