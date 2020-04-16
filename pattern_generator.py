#----------------------------------Global Variable---------------------------------------------------------------
test_case=""
#----------------------------------Alphabet Function-------------------------------------------------------------
def A():
    str1=""
    for i in range(7):
        for j in range(5):
            if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and j in [1,2,3]):
                str1 = str1 + "*"
            else:
                str1 = str1 + " "
        str1 = str1 + "\n"
    return str1

def B():
    str1=""
    for i in range(7):
        for j in range(5):
            if (i in [0,3,6] and j in [1,2,3]) or (j==0 and i<7) or (j==4 and i in [1,2,4,5]):
                str1 = str1 + "*"
            else:
                str1 = str1 + " "
        str1 = str1 + "\n"
    return str1

def C():
    for i in range(7):
        for j in range(5):
            if (j==0 and i in range(1,6)) or (j>0 and i in [0,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def D():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or ((j in range(1,4)) and i in [0,6]) or (j==4 and i in range(1,6)):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def E():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j>0 and i in [0,3,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def F():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j>0 and i in [0,3]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def G():
    for i in range(7):
        for j in range(5):
            if (j==0 and i in range(1,6)) or (j>0 and i==0) or (j in [1,2,3] and i==6) or (j==4 and i in [4,5]) or (j in [2,3] and i==3):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def H():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i<7) or (j in [1,2,3] and i==3):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def I():
    for i in range(7):
        for j in range(5):
            if (j==2 and i<7) or (j>=0 and i in [0,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def J():
    for i in range(7):
        for j in range(5):
            if (j>=0 and i==0) or (j==4 and i<6) or (j in [1,2,3] and i==6) or (j==0 and i in [4,5]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def K():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j==(4-i)and i in range(0,4)) or (j==(i-2) and i in [4,5,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def L():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j>0 and i==6):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def M():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i<7) or (j==i and i in range(1,3)) or (j==3 and i==1):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def N():
    for i in range(7):
        for j in range(7):
            if (j in [0,6] and i<7) or (j==i):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def O():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i in range(1,6)) or (j in range(1,4) and i in [0,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def P():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j in range(1,4) and i in [0,3]) or (j==4 and i in [1,2]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Q():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i in range(1,6)) or (j in range(1,4) and i in [0,6]) or (j==(i-2) and i in [4,5,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def R():
    for i in range(7):
        for j in range(5):
            if (j==0 and i<7) or (j in range(1,4) and i in [0,3]) or (j==4 and i in [1,2]) or (j==(i-2) and i in [4,5,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def S():
    for i in range(7):
        for j in range(5):
            if (j in [1,2,3] and i in [0,3,6]) or (j==0 and i in [1,2]) or (j==4 and i in [4,5]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def T():
    for i in range(7):
        for j in range(5):
            if (j==2 and i<7) or (j>=0 and i==0):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def U():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i in range(1,6)) or (j in range(1,4) and i==6):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def V():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i in range(1,5)) or (j==2 and i==6) or (j in [1,3] and i==5):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def W():
    for i in range(7):
        for j in range(5):
            if (j in [0,4] and i<7) or (j==(i-2) and i in [4,5,6]) or (j==1 and i==5):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def X():
    for i in range(7):
        for j in range(7):
            if (j==i) or (i==6-j):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Y():
    for i in range(7):
        for j in range(7):
            if (j==i and i in range(0,4)) or (i==6-j and i in range(0,4)) or (j==3 and i>3):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def Z():
    for i in range(7):
        for j in range(7):
            if (i==6-j) or (j in range(0,7)and i in [0,6]):
                print("*",end="")
            else:
                print(" ",end="")
        print()

#------------------------------------Program Function-------------------------------------------------------------
def ask_alphabet():
    global test_case
    test_case = input("Enter the alphabet character to get star pattern : ")

def recognize():
    global test_case
    if test_case in ["A","a"]:
        return A()
    elif test_case in ["B","b"]:
        return B()
    elif test_case in ["C","c"]:
        return C()
    elif test_case in ["D","d"]:
        return D()
    elif test_case in ["E","e"]:
        return E()
    elif test_case in ["F","f"]:
        return F()
    elif test_case in ["G","g"]:
        return G()
    elif test_case in ["H","h"]:
        return H()
    elif test_case in ["I","i"]:
        return I()
    elif test_case in ["J","j"]:
        return J()
    elif test_case in ["K","k"]:
        return K()
    elif test_case in ["L","l"]:
        return L()
    elif test_case in ["M","m"]:
        return M()
    elif test_case in ["N","n"]:
        return N()
    elif test_case in ["O","o"]:
        return O()
    elif test_case in ["P","p"]:
        return P()
    elif test_case in ["Q","q"]:
        return Q()
    elif test_case in ["R","r"]:
        return R()
    elif test_case in ["S","s"]:
        return S()
    elif test_case in ["T","t"]:
        return T()
    elif test_case in ["U","u"]:
        return U()
    elif test_case in ["V","v"]:
        return V()
    elif test_case in ["W","w"]:
        return W()
    elif test_case in ["X","x"]:
        return X()
    elif test_case in ["Y","y"]:
        return Y()
    elif test_case in ["Z","z"]:
        return Z()
#------------------------------Main Function----------------------------------------------------------------------
def main():
    ask_alphabet()
    recognize()
#--------------------------------Initializing Program-------------------------------------------------------------
main()