from matplotlib import pyplot
import numpy as np

def calcS(s, a, i): 
    return s - (a*s*i)

def calcI(s, a, i, rate): 
    return i + (a * s * i) - (rate * i)

def calcR(r, rate, i): 
    return r + rate*i

def main(): 
    L = 30
    N = 400
    I = 5
    S = N-I
    I1 = 8
    r = .5
    a = (I1-I+r*I)/(I*S)
    iArr = [I]
    sArr = [N-I]
    rArr = [0]

    for i in np.arange(1, L+1): 
        sArr.append(calcS(sArr[i-1], a, iArr[i-1]))
        iArr.append(calcI(sArr[i-1], a, iArr[i-1], r))
        rArr.append(calcR(rArr[i-1], r, iArr[i-1]))

    pyplot.plot(sArr, 'bo')
    pyplot.plot(iArr, 'ro')
    pyplot.plot(rArr, 'go')
    pyplot.show()

if __name__ == "__main__": 
    main() 
