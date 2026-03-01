qaws={}
class priocomp():
    def add(a,imp):
        qaws[len(qaws)]=[a,imp]
    def clear():
        global qaws
        del qaws
        qaws={}
    def get():
        largest=-1
        idx=0
        for i in range(len(qaws)):
            if int(qaws[i][1])>largest and int(qaws[i][1])>-1:
                largest=int(qaws[i][1])
                idx=i
        if largest==-1:
            return "Use pc.add() to create a new comparison!"
        a=qaws[idx][0]
        qaws[idx][1]=-1
        if "import" in a or "__" in a or "'" in a or '"' in a or "(" in a:
            return "Error: Comparison might be harmful!"
        else:
            a=eval(a)
        if a:
            return True
        else:
            return False
    def remove(idx):
        qaws[idx][1]=-1
    def peek():
        largest=-1
        idx=0
        for i in range(len(qaws)):
            if int(qaws[i][1])>largest and int(qaws[i][1])>-1:
                largest=int(qaws[i][1])
                idx=i
        if largest==-1:
            return "Use pc.add() to create a new comparison!"
        a=qaws[idx][0]
        return a
    def size():
        a=0
        for i in range(len(qaws)):
            if int(qaws[i][1])>-1:
                a+=1
        return a
    def is_empty():
        a=-1
        for i in range(len(qaws)):
            if int(qaws[i][1])>a and int(qaws[i][1])>-1:
                a=int(qaws[i][1])
        return True if a==-1 else False
    def list_all():
        return qaws
pc=priocomp