'''
Created on 15-Oct-2018

@author: User
'''


def paginate_lists(input_arr):
    '''
    host_ids=[]
    num_pages = pages
    records = num_records
    
    for x in input:
        a=x.split(",")
        host_ids.append(a[0])
        
    host_ids = map(int,host_ids)
    print host_ids
    
    num_lists = records/num_pages
    lists=[[]for i in range(num_lists)]
    for i in range(len(host_ids)):
    ''' 
    max = input_arr[0]
    page_data = input_arr[2:]
    ids = set()
    inserted = set()
    pages =[]
    i = 0
    count = 0
    while(i<len(page_data)):
        if (len(pages)-count)%max == 0 and len(ids)>0:
            ids = set()
            i =0
            count +=1
            pages.append(" ")
            
        if page_data[i][0] in ids or i in inserted:
            i+=1
            continue
        ids.add(page_data[i][0])
        pages.append(page_data[i])
        inserted.add(i)
        i+=1
    
    for i in range(len(page_data)):
        if i not in inserted:
            pages.append(page_data[i]) 
            if (len(pages)-count)%max == 0:
                count +=1
                pages.append(" ")
    return pages
    


a = [5, 
    17, 
    "1,28,310.6,SF", 
    "4,5,204.1,SF", 
    "20,7,203.2,Oakland", 
    "6,8,202.2,SF",
    "6,8,202.2,SF",
    "6,8,202.2,SF",
    "6,8,202.2,SF",
    "6,8,202.2,SF", 
    "6,10,199.1,SF", 
    "1,16,190.4,SF", 
    "6,29,185.2,SF", 
    "7,20,180.1,SF", 
    "6,21,162.1,SF", 
    "2,18,161.2,SF", 
    "2,30,149.1,SF", 
    "3,76,146.2,SF", 
    "2,14,141.1,San Jose" 
]
res = paginate_lists(a)
for i in range(len(res)):
    print res[i]
