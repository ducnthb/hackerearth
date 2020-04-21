import time
import random
import queue

def bfs(adj, vis, v):
    Q = queue.Queue(0)
    Q.put(v)
    vis[v] = 0
    res = [1, 0]
    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
            if vis[v] == -1:
                Q.put(v)
                vis[v] = abs(vis[u] - 1)
                res[vis[v]] +=1
    return max(res[0], res[1])

def solve(fin, fou):
    fi = open(fin)
    fo = open(fou, 'w')
    Test = int(fi.readline())
    N = 20005
    for _ in range(Test):
        n = int (fi.readline())
        adj = [set() for j in range(N)]
        visit = [-1]*N
        isThere = [False]*N
        for i in range(n):
            u, v = map(int, fi.readline().split())
            u -= 1
            v -= 1
            isThere[u] = isThere[v] = True
            adj[u].add(v)
            adj[v].add(u)
        res = 0
        for j in range(N):
            if (visit[j] == -1) and isThere[j]:
                res += bfs(adj, visit, j)
        fo.write('%s\n' % res)
    fi.close()
    fo.close()

#solve("data.i0", "data.o0")
#exit()

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
