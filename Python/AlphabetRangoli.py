def print_rangoli(size):
    # your code goes here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = "-".join(alpha[size-1:x:-1] + alpha[x:size])
        print(line.center(4*size-3, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
