
i=check_score(movies[3])
if(i):
    print ('True')
else :
    print ('False')

output_list=sublist_score(movies)
print (output_list)



#Ex3
def return_category(movies,cat_name): 
    output_list=[]
    for i in movies:
        cop_cat=i['category']
        if cat_name==cop_cat:
            output_list.append(i)
    return output_list
    
    
output_list=return_category(movies,'Romance')
print (output_list)



#Ex4
def avg_imdb(movies): 
    avg=0
    total=len(movies)
    for i in movies:
        avg += i['imdb']
    avg=avg/total
    return avg

score=avg_imdb(movies)
print (score)



#Ex5
def avg_category(movies,cat_name): 
    output_list=[]
    for i in movies:
        cop_cat=i['category']
        if cat_name==cop_cat:
            output_list.append(i)
    
    avg=0
    total=len(output_list)
    for i in output_list:
        avg += i['imdb']
    avg=avg/total
    return avg


output_list=avg_category(movies,'Thriller')
print (output_list)