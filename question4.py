def main():
    array =   [0,1,0,2,1,0,1,3,2,1,2,1]
    total_water_cubes = 0
    print water_cube_count(array, total_water_cubes)

def water_cube_count(array, total_water_cubes):
    len_array = len(array)
    positions = 0
    only_values_zero = True
    list_index = 0
    water_cubes = 0
     
    while (list_index < len_array):
        if array[list_index] > 0:
            for auxiliar_index in range(list_index + 1, len_array):
                if array[auxiliar_index] == 0:
                    positions += 1
                elif array[auxiliar_index] != 0:
                    water_cubes = positions
                    list_index = auxiliar_index - 1
                    break
        list_index += 1

    total_water_cubes = water_cubes
    auxiliar_array, only_values_zero = get_auxiliar_array(array, only_values_zero)
    if not only_values_zero:
        water_cubes += water_cube_count(auxiliar_array, total_water_cubes)
    return water_cubes
    

def get_auxiliar_array(array, only_values_zero):
    auxiliar_array = []
    auxiliar_number = 0
    
    for array_number in array:
        if array_number != 0:
            only_values_zero = False
            auxiliar_number = array_number - 1
        else:
            auxiliar_number = 0
        auxiliar_array.append(auxiliar_number)
    
    return auxiliar_array, only_values_zero

if __name__ == '__main__':
    main()