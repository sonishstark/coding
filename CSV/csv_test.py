from csv import reader
 
 
def load_csv(filename):
    csv_data = {}
    file = open(filename,"r")
    lines = reader(file)
    data = list(lines)
    for index in range(len(data)):
        if index == 0:
            for col in data[index]:
                csv_data[col]=[]
        else:
            _index = 0
            for col in csv_data.keys():
                csv_data[col].append(data[index][_index])
                _index+=1

    return csv_data

def search(data,col_key,value):
    ans = [[col for col in data.keys()]]
    found_list = []
    for _ in range(len(data[col_key])):
        if data[col_key][_].lower() == value.lower():
            found_list.append(_)
    for index in found_list:
        ans.append([data[col][index] for col in data.keys()])

    return ans

file_path = "data.csv"
data = load_csv(file_path)

print(data)
print("Enter any one of the following data : ")
x = input("Name - Emplpyee_ID - DOB - Designation - Location : ")
y = input("Enter the name or value of data that needs to be retrieved: ")


print(search(data,x,y))

