t_list: list = []
shoot_id_list: list = []
pi = []


def op_addition(target_list):
    tmp_l = target_list.copy()
    tl_sum = tl_sum = target_list[1] + target_list[2] + target_list[3] + target_list[4]

    if tl_sum == 24:
        shoot_id_list.append(tmp_l[1])
        for i in range(2, 5):
            shoot_id_list.append('+')
            shoot_id_list.append(tmp_l[i])

    if tl_sum == 6:
        if 2 in tmp_l:
            shoot_id_list.append(2)
            tmp_l.remove(2)
            shoot_id_list.append(tmp_l[1])
            tmp_l.pop(1)
            shoot_id_list.append('+')
            shoot_id_list.append(tmp_l[1])
            tmp_l.pop(1)

            list_24 = shoot_id_list[0] * 10 + shoot_id_list[1] + shoot_id_list[3]

            if list_24 != 24:
                shoot_id_list.append('+')
                shoot_id_list.append(tmp_l[1])
        else:
            shoot_id_list.append(1)
            for i in range(2):
                tmp_l.pop(tmp_l.index(1))
            shoot_id_list.append(tmp_l[1])
            shoot_id_list.append('+')
            shoot_id_list.append(1)
            shoot_id_list.append(tmp_l[2])

    if tl_sum == 15:
        if 1 in tmp_l:
            shoot_id_list.append(1)
            tmp_l.remove(1)
            shoot_id_list.append(tmp_l[1])
            for i in range(2, 4):
                shoot_id_list.append('+')
                shoot_id_list.append(tmp_l[i])

    if 7 <= tl_sum <= 14:
        r = tl_sum - 6
        tmp_l.remove(r)
        if 2 in tmp_l:
            shoot_id_list.append(2)
            tmp_l.remove(2)
            shoot_id_list.append(tmp_l[1])
            shoot_id_list.append('+')
            shoot_id_list.append(tmp_l[2])

    if 16 <= tl_sum <= 23:
        r = tl_sum - 15
        tmp_l.remove(r)
        if 1 in tmp_l:
            shoot_id_list.append(1)
            tmp_l.remove(1)
            shoot_id_list.append(tmp_l[1])
            shoot_id_list.append('+')
            shoot_id_list.append(tmp_l[2])

    if 25 <= tl_sum <= 33:
        r = tl_sum - 24
        tmp_l.remove(r)
        shoot_id_list.append(tmp_l[1])
        for i in range(2, 4):
            shoot_id_list.append('+')
            shoot_id_list.append(tmp_l[i])


def op_subtraction(target_list):
    i = 0
    list_24 = 0
    tmp_l = target_list.copy()
    while list_24 != 24 and i != 14:
        j = i + 6
        if i in tmp_l and j in tmp_l:
            pi.append(tmp_l.index(i))
            tmp_l.remove(i)
            pi.append(tmp_l.index(j))
            tmp_l.remove(j)
            if 3 in tmp_l:
                shoot_id_list.append(3)
                shoot_id_list.append(i)
                shoot_id_list.append('-')
                shoot_id_list.append(j)
                list_24 = 24
            else:
                if tmp_l[2] > tmp_l[1]:
                    tmp_l[1], tmp_l[2] = tmp_l[2], tmp_l[1]
                if tmp_l[1] - tmp_l[2] == 3:
                    shoot_id_list.append(tmp_l[1])
                    shoot_id_list.append(i)
                    shoot_id_list.append('-')
                    shoot_id_list.append(tmp_l[2])
                    shoot_id_list.append(j)
                    list_24 = 24
        i += 1

    if list_24 != 24:
        i = 4
        tmp_l = target_list.copy()
        while list_24 != 24 and i != 9:
            j = i - 4
            if i in tmp_l and j in tmp_l:
                pi.append(tmp_l.index(i))
                tmp_l.remove(i)
                pi.append(tmp_l.index(j))
                tmp_l.remove(j)
                if 2 in tmp_l:
                    shoot_id_list.append(2)
                    shoot_id_list.append(i)
                    shoot_id_list.append('-')
                    shoot_id_list.append(j)
                    list_24 = 24
                else:
                    if tmp_l[2] > tmp_l[1]:
                        tmp_l[1], tmp_l[2] = tmp_l[2], tmp_l[1]
                    if tmp_l[1] - tmp_l[2] == 2:
                        shoot_id_list.append(tmp_l[1])
                        shoot_id_list.append(i)
                        shoot_id_list.append('-')
                        shoot_id_list.append(tmp_l[2])
                        shoot_id_list.append(j)
                        list_24 = 24
            i += 1

    if list_24 != 24:
        i = 1
        while list_24 != 24 and i <= 18:
            tmp_l = target_list.copy()
            c = 24 + i
            tens = c // 10
            ones = c % 10
            if tens in tmp_l:
                pi.append(tmp_l.index(tens))
                tmp_l.remove(tens)
                if ones in tmp_l:
                    pi.append(tmp_l.index(ones))
                    tmp_l.remove(ones)
                    if i in tmp_l:
                        shoot_id_list.append(tens)
                        shoot_id_list.append(ones)
                        shoot_id_list.append('-')
                        shoot_id_list.append(i)
                        list_24 = 24
                    else:
                        if tmp_l[1] + tmp_l[2] == i:
                            shoot_id_list.append(tens)
                            shoot_id_list.append(ones)
                            shoot_id_list.append('-')
                            shoot_id_list.append(tmp_l[1])
                            shoot_id_list.append('-')
                            shoot_id_list.append(tmp_l[2])
                            list_24 = 24
                        else:
                            tmp_l = target_list.copy()
            i += 1


def op_division(target_list):
    for i in range(1, 10):
        tmp_l = target_list.copy()
        if i in tmp_l:
            tmp_l.remove(i)
            j = i * 24
            ones = j % 10
            j //= 10
            tens = j % 10
            j //= 10
            if j != 0:
                hundreds = j
                if ones in tmp_l and tens in tmp_l and hundreds in tmp_l:
                    shoot_id_list.append(hundreds)
                    shoot_id_list.append(tens)
                    shoot_id_list.append(ones)
                    shoot_id_list.append('/')
                    shoot_id_list.append(i)
                    break
            elif ones in tmp_l and tens in tmp_l:
                shoot_id_list.append(tens)
                shoot_id_list.append(ones)
                shoot_id_list.append('/')
                shoot_id_list.append(i)
                break


def main():
    a = ['-2748', '+1113', '-2473', '-9245', '+7269', '-1294', '-9245', '+7269', '-6096', '/4146', '/7023', '/7230', '/1205', '/6449', '/1289', '-4420', '-2748', '+7278', '-3195', '+1752', '-3978', '+2112', '-3595', '-6312', '-2495', '-3303', '-8754', '-6096', '-6844', '-9795']
    for j in a:
        t_list.clear()
        shoot_id_list.clear()
        pi.clear()
        s_in = j
        t_list.append(s_in[0])
        for i in range(1, 5):
            t_list.append(int(s_in[i]))
        print(t_list)
        op = t_list[0]

        if op == '+':
            op_addition(t_list)
        elif op == '-':
            op_subtraction(t_list)
        elif op == '/':
            op_division(t_list)

        print(shoot_id_list)
        # print(pi)



if __name__ == "__main__":
    main()

