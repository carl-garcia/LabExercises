
def mode(values):
    result = values[0]
    for value in values:
        if values.count(value)>values.count(result):
            result = value
    return result        
       

def median(Values):
    Values.sort()
    lenght = len(Values)
    if lenght%2 == 0:
        return (Values[lenght//2 -1] + Values[lenght//2])/2
    else:
        return Values[lenght//2]

            
def mean(Values):
    return sum(Values)/len(Values)


Values = []
for i in range(6):
    value = int(input("Enter a Value for the list: "))
    Values.append(value)

    print("List:", Values) 
    print("Mode:", mode(Values))
    print("Median:", median(Values))
    print("Mean:", mean(Values)) 

