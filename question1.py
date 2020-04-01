#Return fields index if contains target sum or -1 if not.

def get_target(array, target):

    array_length = len(array)
    for x in range(array_length):
        for y in range(x + 1, array_length):
            if array[x] + array[y] == target:
                return [x,y]
    return -1

def main():
    array = [1,2,3,4,5,6,7,0]
    print get_target(array, 2)
    

if __name__ == '__main__':
    main()
