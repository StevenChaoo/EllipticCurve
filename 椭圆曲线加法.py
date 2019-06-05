import math
import csv

def find_roots():
    '''
    确定椭圆曲线的根
    :return: num_list:所有椭圆曲线上的根
    '''
    num_list = [[0, 0]]

    for i in range(0, MOD):
        num = (int(i)**3 + A*int(i) + B)%MOD
        for j in range(0, MOD):
            new_num = num + j*MOD
            num_sqrt = int(math.sqrt(new_num))
            if new_num == num_sqrt**2:
                Y = int(math.sqrt(new_num))
                num_list.append(([i, Y]))

    return num_list

def find_mod_reverse(a):
    '''
    求给定模的逆运算
    :param a: 需要求逆的数值
    :return: 求逆结果
    '''
    for i in range(1,MOD*MOD):
        if (i*MOD + 1)%int(a) == 0:
            k = (i*MOD + 1)/int(a)
            return k
            break

def mod(i):
    '''
    求模运算
    :param i: 需要求模的数值
    :return: 求模结果
    '''
    result = int(i)%MOD
    return result

def tabulation():
    '''
    根据椭圆曲线上的根制加法表
    '''
    num_list = find_roots()
    row_list = [' '] + num_list
    row_list1 = row_list
    row_list1[1] = '0'

    with open('A='+str(A) + ' B='+str(B) + ' mod='+str(MOD) + '.csv', 'w') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(row_list1)
        print(row_list1)
        for point1 in num_list:
            if point1 == [0, 0]:
                table = ['0']
            else:
                table = [point1]
            for point2 in num_list:
                if point1[0] == point1[1] == 0:
                    target = point2
                elif point2[0]==point2[1]==0:
                    target = point1
                elif point1==point2 and point1[1]==0:
                    target = [0 ,0]
                elif point1 == point2:
                    result1 = (3 * (point1[0]**2) + A) * find_mod_reverse((2*point1[1]))
                    result2 = mod(result1)
                    x3 = result2**2 - point1[0] - point2[0]
                    y3 = result2 * (point1[0] - x3) - point1[1]
                    target = [mod(x3), mod(y3)]
                elif point1[0]==point2[0] and point1[1]!=point2[1]!=0:
                    target = [0, 0]
                elif point1 != point2:
                    x = point2[0] - point1[0]
                    y = point2[1] - point1[1]
                    result1 = y * find_mod_reverse(x)
                    result2 = mod(result1)
                    x3 = result2**2 - point1[0] - point2[0]
                    y3 = result2 * (point1[0] - x3) - point1[1]
                    target = [mod(x3), mod(y3)]

                if target == [0, 0]:
                    table.append('0')
                else:
                    table.append(target)
            writer.writerow(table)
            print(table)
        csvf.close()

if __name__ == '__main__':
    print('\nY^2 = X^3 + AX +B (mod MOD)\n')
    MOD = int(input('mod = '))
    A = int(input('A = '))
    B = int(input('B = '))

    tabulation()