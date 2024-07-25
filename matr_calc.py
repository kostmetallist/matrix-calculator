def fun0():

    return input("\nЧто делать дальше? Ввести ещё одну матрицу (more),\
 взглянуть на одну из них (look), транспонировать одну из них (tp),\
 умножить (mul), сложить (add), вычесть (sub), умножить на скаляр (scal)? Чтобы выйти,\
 нажать Enter.\n\n")


def avlbl():

    print("\nДоступные матрицы:", *base.keys())


def save(lis):

    while 1:
        anw = input("\nСохранить эту матрицу? (yes/no) ")
        if anw == 'yes':
            name = input("Введите имя (старые имена могут\
 быть перезаписаны) ")
            base[name] = lis
            break

        elif anw == 'no':
            pass
            break

        else:
            print("\nНе понял. Пробуй ещё. ")
            continue


def scan(inp):

    if '.' in inp:
        return float(inp)

    else:
        return int(inp)

#def addition(A,B):

    

base = {}
c = 0
inp = input("Ввести матрицу построчно, завершить ввод пустой строкой.\
 Элементы разделять пробелами.\
 Введённая матрица будет обозначена как A.\n\n")

lis = []
            
while inp:
    lis.append(inp.split())
    inp = input()
            
base["A"] = lis
            
act = fun0()

while act:
            
    if act == 'more':

        name = input("\nВведите имя новой матрицы - ")
        inp = input("Ввести матрицу построчно, завершить\
 ввод пустой строкой. Элементы разделять пробелами.\n\n")
            
        lis = []
                
        while inp:
            lis.append(inp.split())
            inp = input()

        base[name] = lis
        act = fun0()
        continue
        
    elif act == 'look':

        while 1:
            avlbl()
            obj = input("На какую? ")

            if obj in base:
                print()
                for i in base[obj]:
                    print(*i)
                break

            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue
            
        act = fun0()
        continue
        
    elif act == 'tp':

        while 1: 
            avlbl()
            obj = input("Какую? ")
            print()

            if obj not in base.keys():
                print("\nТакой нет. Пробуй ещё. ")
                continue

            else:
                strok = len(base[obj][0])
                lis = [[] for i in range(strok)]
                c = 0

                while c < strok:
                    for i in base[obj]:
                        lis[c].append(i[c])
                    c += 1

                for j in lis:
                    print(*j)
                break
            
        save(lis)
        act = fun0()
        continue

    elif act == 'mul':

        avlbl()

        while 1:
            first = input("\nПервая: \n\n")

            if first in base.keys():
                break

            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        while 1:
            second = input("\n\nВторая: \n\n")

            if second in base.keys():
                break

            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        if len(base[first][0]) != len(base[second]):
            print("\nА их нельзя умножать. Вернёмся назад.")
            act = fun0()
            continue

        else:
            str1, sto2 = len(base[first]), len(base[second][0])
            i = 0
            res = [[]*y for y in range(str1)]
            lis = []
            
            while i < str1:
                j = 0
                while j < sto2:
                    EL = 0
                    for u,v in enumerate(base[first][i]):
                        EL += scan(v)*scan(base[second][u][j])
                    res[i].append(str(EL))
                    j += 1
                i += 1

            print()

            for z in res:
                print(*z)

            save(res)
        act = fun0()
        continue

    elif act == 'add':
        
        avlbl()

        while 1:
            first = input("\nПервая: \n\n")
            if first in base.keys():
                break
            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        while 1:
            second = input("\n\nВторая: \n\n")
            if second in base.keys():
                break
            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        str1 = len(base[first])
        sto1 = len(base[first][0])

        if str1 != len(base[second]) or\
 len(base[first][0]) != len(base[second][0]):
            print("\nА их нельзя складывать. Вернёмся назад.")
            act = fun0()
            continue

        else:
            res = [[]*i for i in range(str1)]
            i = 0

            while i < str1:
                j = 0
                while j < sto1:
                    res[i].append(scan(base[first][i][j])\
 + scan(base[second][i][j]))
                    j += 1
                i += 1

            for z in res:
                print(*z)

            save(res)
        act = fun0()
        continue

    elif act == 'sub':

        avlbl()

        while 1:
            first = input("\nПервая: \n\n")
            if first in base.keys():
                break
            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        while 1:
            second = input("\n\nВторая: \n\n")
            if second in base.keys():
                break
            else:
                print("\nТакой нет. Пробуй ещё. ")
                continue

        str1 = len(base[first])
        sto1 = len(base[first][0])

        if str1 != len(base[second]) or\
 len(base[first][0]) != len(base[second][0]):
            print("\nА их нельзя складывать. Вернёмся назад.")
            act = fun0()
            continue

        else:
            res = [[]*i for i in range(str1)]
            i = 0

            while i < str1:
                j = 0
                while j < sto1:
                    res[i].append(scan(base[first][i][j])\
 + scan(base[second][i][j]))
                    j += 1
                i += 1

            for z in res:
                print(*z)

            save(res)
        act = fun0()
        continue

    elif act == 'scal':

        while 1: 
            avlbl()
            obj = input("Какую? ")

            if obj not in base.keys():
                print("\nТакой нет. Пробуй ещё. ")
                continue

            else:
                num = scan(input("На какое число умножить? "))
                lis = [[]*i for i in range(len(base[obj]))]
                print()
                for i in range(len(base[obj])):
                    for j in range(len(base[obj][0])):
                        lis[i].append(str(scan(base[obj][i][j])*num))

            for z in lis:
                print(*z)

            break

        save(lis)
        act = fun0()
        continue
        
    else:
        print("Непонятно. Давай заново.\n")
        act = fun0()
        continue
