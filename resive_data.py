import random
global ffname
global sq

error_ratio = 0.000000

def error_or_not():
    ra = random.randrange(0,int(sq))
    if(ra <= sq*error_ratio):
        return True
    return False

def error(dict,seqnumber):    #simple error checking
    for i,j in dict.items():
        for p,q in j.items():
            if( p == q.__hash__() and (seqnumber == i)):
               # simulation error using uniform distributuion
                if(error_or_not()):
                   return False
                return True
    return False

def writer(orfile):
    f = open(ffname, 'wb')
    for i in orfile:
        f.write(i)
    f.close()

def datapart(dict):
    for i,j in dict.items():
        for p,q in j.items():
            return q

def window_number(dict):
    for i,j in dict.items():
        return i

def print_All(time,errors,noterrors):
    print("\n------- Results-------")
    print("Time " + time)
    print("File resived compleatly")
    print("Error packets resived " + str(errors))
    print("Error free resived "+ str(noterrors))
    print("Total packets "+ str(errors+noterrors))
    print("Error ratio "+ str(errors/(errors+noterrors)))

