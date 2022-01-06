from collections import Counter
import csv
with open("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

#print(file_data)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(float(num))

data=Counter(new_data)
range={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,    
    "155-165":0,
    "165-175":0,
}
for weight,occurence in data.items():
    if 75<weight<85:
        range["75-85"]+=occurence
    elif 85<weight<95:
        range["85-95"]+=occurence
    elif 95<weight<105:
        range["95-105"]+=occurence
    elif 105<weight<115:
        range["105-115"]+=occurence
    elif 115<weight<125:
        range["115-125"]+=occurence
    elif 125<weight<135:
        range["125-135"]+=occurence
    elif 135<weight<145:
        range["135-145"]+=occurence
    elif 145<weight<155:
        range["145-155"]+=occurence
    elif 155<weight<165:
        range["155-165"]+=occurence
    elif 165<weight<175:
        range["165-175"]+=occurence

moderange,modeoccurence=0,0
for range,occurence in range.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((moderange[0]+moderange[1])/2)
print(mode)





















