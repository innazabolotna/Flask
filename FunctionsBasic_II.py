print("/")
def countdown(n):
    list_of_count_down=[]
    while(n>0):
        list_of_count_down.append(n)
        print(list_of_count_down)
        n=n-1
    return list_of_count_down
countdown(5)

print("/")
def list_with_two_number(list):
    for i in range(len(list)):
        print(list[0])
        return list[1]
list_with_two_number([1,2])

print("/")
def first_plus_length(list):
    x=list[0]+len(list)
    print(x)
    return x
first_plus_length([1,2,3,4,5])

print("/")
def values_greater_than_second(list):
    if len(list)<2:
        return false
    new_list=[]
    for i in list:
        if(i>list[1]):
            new_list.append(i)
    print(len(new_list))
    return new_list
print(values_greater_than_second([5,2,3,2,1,4]))
def this_length_that_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
print(this_length_that_value(4,7))