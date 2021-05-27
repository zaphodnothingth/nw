# ia = IMDb()

# MoviesList=[]
# Title=[]
# Year=[]
# Actors=[]

# s=0
# for p in starting_page:
#     page = requests.get(p)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     movies = soup.findAll('div', attrs={'class' : 'filmo-row'})  
#     for movie in movies:
#         mid=movie.a['href'].replace("/title/tt","").replace("/","")
#         if mid not in MoviesList:
#             MoviesList.append(mid)

# MoviesList=list(set(MoviesList))
# print(len(MoviesList)) 

# movies=[]
# for i,mo in enumerate(MoviesList):
#     movie = ia.get_movie(mo)
#     try:
#         actors=[a['name'] for a in movie['actors']]
#         if your_actor in actors:
#             try:
#                 km=str(movie['kind'])
#                 dte=movie['original air date'].split(" (")[0]
#                 if km=="movie" and 'genres' in movie.keys() and "Short" not in str(movie['genres']):
#                     s+=1
#                     Title.append(movie['title'])
#                     Year.append(movie['year'])
#                     print(s,movie['title'],"in",movie['year']) #"directed by",drct,
#                     SRS=[]
#                     try:
#                         for actor in movie['actors']: #[:5]:
#                             if actor['name']!=your_actor:
#                                 SRS.append(actor['name'])
#                     except:
#                         SRS.append('nan')
#                     Actors.append(', '.join(SRS))
#                 if km=="movie" and 'genres' not in movie.keys():
#                     s+=1
#                     Title.append(movie['title'])
#                     Year.append(movie['year'])
#                     print(s,movie['title'],"in",movie['year']) #"directed by",drct,
#                     SRS=[]
#                     try:
#                         for actor in movie['actors']: #[:5]:
#                             if actor['name']!=your_actor:
#                                 SRS.append(actor['name'])
#                     except:
#                         SRS.append('nan')
#                     Actors.append(', '.join(SRS))
#             except:
#                 s+=0
#                 pass
#     except:
#         print(i,"NOT HERE")

# print(len(Title),len(Year),len(Actors)) #len(Date),len(Director),len(Plot)),len(Genre)
        
# Films = pd.DataFrame(
#     {'Title':Title,
#      'Year':Year, 
#      'Actors':Actors,
#     })
# Films=Films[['Title','Year','Actors']] 
# print(len(Films))
# Films.sort_values(by=['Year'], ascending=True)
