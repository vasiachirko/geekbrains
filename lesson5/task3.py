SALARY_BORDER = 20000
with open('firm.txt', 'r') as fp:
    str = fp.readlines()
    for i in str:
        sn, zp = i.split()
        zp_int = int(zp)
        if zp_int < SALARY_BORDER:
            print(sn, zp_int)
    a = [x.split() for x in str]
    zps = []
    for x in a:
        sn, zp = x
        zps.append(int(zp))
    print(f'{sum(zps)/len(zps):.2f}')