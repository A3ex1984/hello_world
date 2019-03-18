# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

#variable for amount of classrooms

#for i in array compare if end time is smaller than start time
#if overlap, increase number_classrooms

def classroom_calculation (class_times):
    number_classrooms = 1
    for x in class_times:
        for y in class_times:
            if x[0]>y[0] and x[0]<y[1]:
                number_classrooms += 1

    return number_classrooms


#print amount of needed classrooms for given array
print (classroom_calculation([(30, 75), (0, 50), (60, 150)]))


def find_nr_rooms(intervals):
    max_rooms = 0
    for v in intervals:
        rooms=1
        for u in intervals:
            if u[0]>v[0] and u[0]<v[1]:
                rooms += 1
        if rooms > max_rooms: max_rooms = rooms      
    return max_rooms

lectures = [(30, 75), (0, 50), (60, 150)]
print('Max Rooms', find_nr_rooms(lectures))       