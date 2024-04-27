def median(input):
    input.sort()
    number=len(input)
    mid=int(number/2);
    if(number%2==1):
        return input[mid]
    else:return (input[mid-1]+input[mid])/2
  
def mean(input):
    number=len(input)
    sum=0
    for i in input:
        sum=sum+i;
    return sum/number


def mode(input):
    output = max(set(input), key = input.count)
    return output
