class Overlapping:  
    def overlap(inputed_array, n):
        found_overlapped_array = []
        temp_array = []
        if inputed_array == []:
            return []
        else:
            sorted_array = sorted(inputed_array, key=lambda x: x[1])
            for i in range (0, n-1):
                if sorted_array[i][0] < sorted_array[i][1]:
                    for j in range(i+1, n):
                       if sorted_array[j][0] < sorted_array[j][1] and sorted_array[j][0] < sorted_array[i][1] :
                            temp_array = []
                            temp_array.append([int(sorted_array[i][0]), int(sorted_array[i][1])])          
                            temp_array.append([int(sorted_array[j][0]), int(sorted_array[j][1])])
                            found_overlapped_array.append(temp_array)      
            return found_overlapped_array
