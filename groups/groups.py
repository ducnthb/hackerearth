import time
import random

def find(u, pa):
    while pa[u] != u:
        u = pa[u]
    return pa[u]

def union(u, v, pa, ra):
    u = find(pa[u], pa)
    v = find(pa[v], pa)
    if u == v:
        return
    if ra[u] > ra[v]:
        pa[v] = pa[u]
        ra[u] += ra[v]
    else:
        pa[u] = pa[v]
        ra[v] += ra[u]

def solve(fin, fou):
    fi = open(fin)
    fo = open(fou,'w')
    n, m = map(int, fi.readline().split())
    pa = [i for i in range(n)]
    ra = [1 for i in range(n)]
    for i in range(m):
        u, v = map(int, fi.readline().split())
        u -= 1
        v -= 1
        union(u, v, pa, ra)

    res = 1
    MOD = 1000000007
    for i in range(n):
        if pa[i] == i:
            res = ((res % MOD)  * (ra[i]% MOD)) % MOD
    fo.write("%s\n" % res)

solve("data.i0", "data.o0")
exit()

cnt = 0
fname = "data"
while cnt < 10:
    cnt +=1
    fin = fname+".i"+str(cnt)
    fou = fname+".o"+str(cnt)
    '''
    fi = open(fin,'w')
    random.seed(time.time())
    test = random.randint(1,50)
    fi.write("%s\n" % test)
    for t in range(test):
        edges = []
        n = random.randint(1,200)
        edges = gen_random_edgeList(n)
        if not check3(n, edges):
            print(fin + " - Test " + str(t+1) +" khong hop le")
        fi.write("%s % s\n" % (n, len(edges)))
        for i in range(len(edges)):
            fi.write("%s % s\n" % (edges[i][0]+1, edges[i][1]+1))
        if test:
            fi.write("\n")
    fi.close()
    '''
    ti = time.time()
    solve(fin, fou)
    print("test %s running time : %f" % (cnt, (time.time() - ti)))
