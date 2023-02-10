def check_score(movie): 
    if(movie['imdb']>5.5):
        return True
    else:
        return False
        
        
i=check_score(movies[3])
if(i):
    print ('True')
else :
    print ('False')
