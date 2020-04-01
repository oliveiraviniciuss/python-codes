def main():
    array =   [10,1,5,3,0,23]
    print get_max_gain(array)

def get_max_gain(array):
    max_gain = 0
    len_array = len(array)
    for x in range(len_array):
        for y in range(x + 1,len_array):
            if array[y] - array[x] > max_gain:
                max_gain = array[y] - array[x]
    return max_gain

if __name__ == '__main__':
    main()