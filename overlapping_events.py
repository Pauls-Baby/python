class Overlapping:
    
    def overlap(inputed_array, n):
        overlapped_array = []
        sorted_array = sorted(inputed_array, key=lambda x: x[0])
        print(sorted_array)

        for i in range(1, n):
            if sorted_array[i-1][1] > sorted_array[i][0]:
                overlapped_array.append([int(sorted_array[i-1][0]), int(sorted_array[i-1][1])])
                overlapped_array.append([int(sorted_array[i][0]), int(sorted_array[i][1])])
                return True , overlapped_array 

        return False , []


    event_array = []
    tot_event_array = []
    overlapped_array = []

    while True:
        print("----------------MENU------------------")
        print("1 - Schedule event")
        print("q - Quit")
        print(" ")
        action = input("Enter your choice : ")

        if action == "q" : break

        elif action == "1":
            start_time = int(input("Enter event starting time : "))
            end_time = int(input("Enter event ending time : "))

            if start_time < end_time:
                event_array = [int(start_time), int(end_time)]
                print(event_array, 'is added')
                tot_event_array.append(event_array)
            else:
                print("Invalid schedule")

            print(tot_event_array)

        else:
            print("Invalid input")

    n = int(len(tot_event_array))
    print(n)
    if n == 1:
        print("Single event only")
    else:
        overlap_exist , overlapped_array = overlap(tot_event_array, n)

        result = True if overlap_exist else False
        if result == True:
            result = "Overlapping schedule"
        else:
            result = "Not overlapping"
        print(result)
        print("Overlapping events: ",overlapped_array)

