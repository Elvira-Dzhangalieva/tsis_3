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