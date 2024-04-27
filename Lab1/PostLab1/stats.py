def median(input):
    input.sort()
    number=len(input)
    mid=int(n/2);
    if(n%2==1):
        return input[mid]
    else:return (input[mid-1]+input[mid])/2
  
def mean(input):
    number=len(input)
    sum=0
    for i in a:
        sumofa=sumofa+i;
    return sum/number


def mode(input):
    output = max(set(input), key = input.count)
    return output
