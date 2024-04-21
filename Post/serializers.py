from rest_framework import serializers
from .models import Post 
from users.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'last_name',  'email', 'get_image', 'get_background', 'profile_pic' , 'background' , 'artistname' ]
        
    #FILTER USER POST   
    def user_posts(self, account):
        posts = Post.objects.filter(account=account)
        return PostSerializer(posts, many=True).data







class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default='avatar.png'  ,allow_empty_file=False)
    track = serializers.FileField(default='avatar.png' ,max_length=None,allow_empty_file=False )
    title = serializers.CharField(default='avatar.png',max_length=250 )
    description = serializers.CharField(default='avatar.png',max_length=250)
    class Meta:  
        model = Post
        fields = ('id', 'title', 'description' , 'unique_id'  , 'image', 'get_image', 'track', 'tracks')