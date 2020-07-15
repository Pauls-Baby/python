class Overlapping:  
    def overlap(inputed_array, n):
        middle = 0
        adjacent = 0
        found_overlapped_array = []
        temp_array = []
        if inputed_array == []:
            return [], middle, adjacent
        else:
            sorted_array = sorted(inputed_array, key=lambda x: x[0])
            for j in range (0, n):
                for i in range(1, n):
                    if i!=j:
                        if (sorted_array[i][0] >= sorted_array[j][0] and sorted_array[i][1] <= sorted_array[j][1]):             #middle overlaps
                            temp_array = []
                            temp_array.append([int(sorted_array[i][0]), int(sorted_array[i][1])])              
                            temp_array.append([int(sorted_array[j][0]), int(sorted_array[j][1])])
                            middle+=1
                            reversed_list = temp_array[::-1]
                            if temp_array not in found_overlapped_array and reversed_list not in found_overlapped_array:
                                found_overlapped_array.append(temp_array)
                        if j == 0:
                            if (sorted_array[i-1][1] >= sorted_array[i][0]):                                                     #adjacent and overlaps
                                temp_array = []
                                temp_array.append([int(sorted_array[i-1][0]), int(sorted_array[i-1][1])])           
                                temp_array.append([int(sorted_array[i][0]), int(sorted_array[i][1])])
                                adjacent+=1
                                reversed_list = temp_array[::-1]
                                if temp_array not in found_overlapped_array and reversed_list not in found_overlapped_array:
                                    found_overlapped_array.append(temp_array) 
                        if (sorted_array[i][0] >= sorted_array[j][0] and sorted_array[j][1] >= sorted_array[i][0]):             #not adjacent but overlaps
                            temp_array = []
                            temp_array.append([int(sorted_array[j][0]), int(sorted_array[j][1])])           
                            temp_array.append([int(sorted_array[i][0]), int(sorted_array[i][1])])
                            reversed_list = temp_array[::-1]
                            if temp_array not in found_overlapped_array and reversed_list not in found_overlapped_array:
                                found_overlapped_array.append(temp_array)              
            return found_overlapped_array, middle, adjacent                                                                    # found_overlapped_array holds list of the overlapping pairs
