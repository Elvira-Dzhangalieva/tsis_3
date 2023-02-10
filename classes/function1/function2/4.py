def avg_imdb(movies): 
    avg=0
    total=len(movies)
    for i in movies:
        avg += i['imdb']
    avg=avg/total
    return avg

score=avg_imdb(movies)
print (score)