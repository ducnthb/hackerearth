import time
import random
import queue

def bfs(adj, vis, v):
    Q = queue.Queue(0)
    Q.put(v)
    vis[v] = True
    res = 1
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
            if not vis[v]:
                Q.put(v)
                vis[v] = True
                res +=1
    return res

def solve(fin, fou):
    fi = open(fin)
    fo = open(fou, 'w')
    n, m = map(int, fi.readline().split())
    adj = [set() for j in range(n)]
    for i in range(m):
        u, v = map(int, fi.readline().split())
        u -= 1
        v -= 1
        adj[u].add(v)
    res = int(1e9)
    for j in range(n):
        visit = [False]*n
        res = min(res, bfs(adj, visit, j))
    fo.write('%s\n' % res)
    fi.close()
    fo.close()

#solve("data.i4", "data.o4")
#exit()

cnt = 0
fname = "data"
while cnt < 11:
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
