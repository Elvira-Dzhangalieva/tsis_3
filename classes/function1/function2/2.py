def sublist_score(movies): 
    output_list=[]
    for i in range(0,len(movies)):
        cop_movie=movies[i]
        if cop_movie['imdb']>5.5:
            output_list.append(cop_movie)
    return output_list
    
    
output_list=sublist_score(movies)
print (output_list)
