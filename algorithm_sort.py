import time

def bubble_sort(list,key):
 for j in range(0,len(list)-1):
   for i in range(j+1,len(list)):
     if int(list[j][key]) > int(list[i][key]):  
       list[j],list[i] = list[i],list[j]
 return list


def selection_sort(list,key):
    for i in range(0,len(list) - 1):
        min_idx = i
        for j in range(i + 1, len(list)):
            if int(list[j][key]) < int(list[min_idx][key]):
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

def shell_sort(list,key):
     for h in range(5,0,-2):
      for i in range(h,len(list)) :
           CurrentElement= list[i]
           j = i;
           while j>=h and int(list[j-h][key])>int(CurrentElement[key]):
                list[j]=list[j-h]
                j=j-h
           list[j]=CurrentElement
     return list

def merge_sort(list,key):
    if len(list) <= 1 :
        return list
    mid = len(list) // 2
    Left = merge_sort(list[:mid],key)
    Right = merge_sort(list[mid:],key)

    merged_list = []
    l = h = 0
    while l < len(Left) and h < len(Right):
        if int(Left[l][key]) < int(Right[h][key]):
            merged_list.append(Left[l])
            l += 1
        elif int(Left[l][key]) > int(Right[h][key]) :
            merged_list.append(Right[h])
            h += 1
        else:
            merged_list.append(Left[l])
            l += 1
    merged_list += Left[l:]
    merged_list += Right[h:]
    return merged_list


 

csv_file = 'please enter the path which save what you want to sort (csv file)'  #파일 불러오기
f_obj = open(csv_file)
#f=pandas.read_csv('Fighters.csv', names=['name', 'country', 'year', 'number']) #Please modify this according to yours
f = f_obj.read()
f_keys = f.split('\n')
#print(f_keys)
test_list = len(f_keys)
list = []
c_result =[]
count=0
for i in range(0, test_list):
 f_keys = (f.split('\n')[i]).split(',')
 list.append(f_keys)  #2차원 배열 생성
key = 2 #무슨 열을 기준으로 정렬 할 건지, 2: 생산년도, 4: 생산대수 
start = time.time()
list = merge_sort(list,key)  #bubble_sort(list,key),selection_sort(list,key),shell_sort(list,key),merge_sort(list,key)
print("sort time: ",time.time()-start) #코드 수행 시간

#for i in range(0,len(list)): # key에 따라 정렬된 리스트 출력(a(key=2),b(key=4)의 경우)
#  for j in range(0,5):
#    print(list[i][j])
#  print('\n')

#print(list)
#print('-------------------------------------------------------------------------------------')
for i in range(0,len(list)-1): #생산년도(key=2)대로 소트한 후, 생산대수대로 소트하기 출력
  key=2
  if int(list[i][key])==int(list[i+1][key]):
      count+=1
  else:
      arr = list[i-count:i+2]
      key=4
      c_result.append(merge_sort(arr,key))
      count=0
      
#print("sort time: ",time.time()-start) #c 경우 수행 시간
#print(c_result)

