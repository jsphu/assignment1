
def delta(x,y):
    return 0 if x == y else 1

def M(seq1,seq2,i,j,k):
    return max(delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k])) # or sum with a threshold


def makeMatrix(seq1,seq2,k):
    n = len(seq1)
    m = len(seq2)
    return [[M(seq1,seq2,i,j,k) for j in range(m-k+1)] for i in range(n-k+1)]


def plotMatrix(M,t, seq1, seq2, nonblank = chr(0x25A0), blank = ' '):
    print(' |' + seq2)
    print('-'*(2 + len(seq2)))
    for label,row in zip(seq1,M):
        line = ''.join(nonblank if s < t else blank for s in row)
        print(label + '|' + line)


def dotplot(seq1,seq2, window=1, threshold=1):
    M = makeMatrix(seq1,seq2,window)
    plotMatrix(M, t, seq1,seq2)


def dotplot2(seqx, seqy, window, threshold=1):
    import numpy as np
    import matplotlib.pyplot as plt
    #    
    M = np.array(makeMatrix(seqx,seqy,window))
    #
    dotplot=plt.imshow(M, cmap='binary_r')
    if len(seqx) > 50 or len(seqy) > 50:
        plt.tick_params(top=False, labeltop=False, bottom=False, labelbottom=False, left=False, labelleft=False)
    else:
        plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    xt=plt.xticks(np.arange(len(list(seqx)))+.5,list(seqx))
    yt=plt.yticks(np.arange(len(list(seqy)))+.5,list(seqy))

    plt.show()

