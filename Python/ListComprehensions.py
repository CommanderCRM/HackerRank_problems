if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x_list = list(range(x+1))
    y_list = list(range(y+1))
    z_list = list(range(z+1))
    perm_list = [[x,y,z] for x in x_list for y in y_list for z in z_list]
    list_without_sums = [list for list in perm_list if sum(list) != n]
    print(list_without_sums)
