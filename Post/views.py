#RESTFRAMEWORK VIEW
from rest_framework import generics , mixins 


#MODEL 
from .models import Post

#RESTFRAMEWORK RESPONSE
from rest_framework.response import Response


#AUTHENTICATED RESTFRAMEWORK
from rest_framework.permissions import IsAuthenticated 

#SERIALIZER
from .serializers import PostSerializer , UserAccountSerializer

#JSON FOR FORM FRONTEND REACT
from rest_framework.parsers import MultiPartParser, FormParser 



#RETRIVE USER POSTED
class PostViewUser(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)
    def create(self, request):
       account = self.request.user
       serializer = PostSerializer(data=request.data)
       if serializer.is_valid():
            audio_file = serializer.validated_data['track']
            image_file = serializer.validated_data['image']
            title_file = serializer.validated_data['title']
            description_file = serializer.validated_data['description']
            audio_model = Post(track=audio_file , 
                                  account=account , title=title_file 
                                  ,image=image_file , 
                                  description=description_file
                                  
                                  )
            audio_model.save()
            return Response({'message': 'Audio file uploaded successfully'}, status=201)
       else:
            return Response(serializer.errors, status=400)
        
        
    #POST METHOD    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
 
    def perform_create(self, serializer):
        account = self.request.user
        serializer.save(account=account)

    #GET METHOD
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserAccountSerializer(user)
        data = serializer.data
        posts = serializer.user_posts(user)
        data['posts'] = posts
        return Response(data)