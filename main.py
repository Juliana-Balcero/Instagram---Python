from InstagramAPI import InstagramAPI #importo la API free
import time
from datetime import datetime


#Función que retorna la lista de seguidores del usuario
def getTotalFollowers():
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

#Función que me retorna la lista de los que sigue el usuario
def getFollowing():
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following

#Función que me retorna el numero de posts del perfil
def getPosts():
    myposts = []
    has_more_posts = True
    max_id = ""
    while has_more_posts:
        api.getSelfUserFeed(maxid=max_id)
        if api.LastJson['more_available'] is not True:
            has_more_posts = False  # stop condition

        max_id = api.LastJson.get('next_max_id', '')
        myposts.extend(api.LastJson['items'])  # merge lists

    return myposts

#Función que me retorna el numero de comentarios de un post en especifico
def getComent():
    media_id = 'id del post' #le paso el id del post
    has_more_comments = True
    max_id = ''
    comments = []
    while has_more_comments:
        _ = api.getMediaComments(media_id, max_id=max_id)
        #Los comentarios del post vienen desde el mas antiguo hasta el mas nuevo,
        #eso me permite preservar en orden descendiente en la lista completa
        for c in reversed(api.LastJson['comments']):
            comments.append(c)
        has_more_comments = api.LastJson.get('has_more_comments', False)
        if has_more_comments:
            max_id = api.LastJson.get('next_max_id', '')
            time.sleep(2)
    print("Post id: ", media_id)
    return comments

#Función que me retorna lista de los likes del post
def get_likes_list():
    media_id = 'id del post' #le paso el id del post
    api.getMediaLikers(media_id)
    f = api.LastJson['users']
    likes_list = []
    for x in f:
        likes_list.append(x['username'])

    return likes_list

if __name__ == "__main__":
    #datos para usar los servicios de la api
    api = InstagramAPI("username", "password")
    api.login()
    user_id = api.username_id

    # Imprimo el username
    print('Username:@',api.username)

    #En vez de imprimir la lista completa de seguidores, imprimo el tamaño de esta
    followers = getTotalFollowers()
    print('Followers:', len(followers))

    #En vez de imprimir la lista completa de seguidos, imprimo el tamaño de esta
    following = getFollowing()
    print('Following:', len(following))

    #Imprimo el tamaño de la lista de los posts
    myposts = getPosts()
    print('Number of posts:', len(myposts))
    
    #Obtengo el post en especifico con los comentarios
    comments = getComent()

    #Obtengo los likes del post
    likes_list= get_likes_list()

    #Imprimo numero de likes y comentarios
    print('Post likes:', len(likes_list))
    print('Post comments:',len(comments))
