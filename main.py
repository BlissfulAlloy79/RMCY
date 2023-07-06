target_list: list = []
shoot_id_list: list = []
pi = []


def op_minus():
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
            print(i)
            print(tmp_l)
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


def main():
    # s_in = input("Enter sequence")
    s_in = "-3295"
    target_list.append(s_in[0])
    for i in range(1, 5):
        target_list.append(int(s_in[i]))
    print(target_list)

    op_minus()
    print(shoot_id_list)
    # print(pi)


if __name__ == "__main__":
    main()

# TODO: 3195


