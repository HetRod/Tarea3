def validarHora(hour_text):
    n = int(hour_text)
    return (n%100 == 0 and n>=600 and n<=1800)
            
def marzullo_recorrido(ranges2, solicitud):
    table = []
    ranges = list(ranges2)
    ranges.append(solicitud)
    beststart, bestend = 0, 0
    for l,r in ranges:
        table.append((l,-1))
        table.append((r,+1))
    for i in range( len( table ) ):
        for k in range( len( table ) - 1, i, -1 ):
            if ( table[k][0] < table[k - 1][0] ):
                swap( table, k, k - 1 )
            if ( table[k][0] == table[k - 1][0] ):
                if ( table[k][1] > table[k - 1][1] ):
                    swap ( table, k, k - 1 )
 
    best = 0
    cnt = 0
    for i in range(len(table) ):
        cnt = cnt - table[i][1]
        if best < cnt:
            best = cnt
            beststart = table[i][0]
            bestend   = table[i+1][0]
    if (best < 10):
        return True
    elif (beststart < solicitud[1] and bestend > solicitud[0]):
        return False
    return True

def swap(A,x,y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
