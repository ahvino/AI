import pyfacebook
import fb
import facebook

appID = 1313828222853030
token = 'EAASq63iE36YBAPI8MQdPuYKnUNGkUokv1AUoJSYBb2fcCYSz8wX3q5DiYqeYyZAwlcgh66JJxZAqGs4iyyuj6ZC1zfYGAzUhid8IQQpZC4ZAoZBZC3Vbf4TzBVT18smBjKDd2SrJ565NVx3edgnuVUtstOBfynHYkYsr4hwpNciT9d6u9EtAZAdWWXGhAv1eDad8a8l7DyQGA0FiYLAzayMqdv01WWypMIFnSr8CF0SWuGLvAdvRTuNJ'
appToken = '1313828222853030|rYIDd8lwhcnLgM38PDwoF_YiFko'

graph = facebook.GraphAPI(token)
feed = graph.get_object('me/feed')


for post in feed['data']:
    if'message' in post:
        print("Message: " + post['message'])