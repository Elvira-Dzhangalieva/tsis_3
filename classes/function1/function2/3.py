def return_category(movies,cat_name): 
    output_list=[]
    for i in movies:
        cop_cat=i['category']
        if cat_name==cop_cat:
            output_list.append(i)
    return output_list
    
    
output_list=return_category(movies,'Romance')
print (output_list)

