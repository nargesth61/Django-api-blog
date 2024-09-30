from rest_framework import serializers
from ...models import Posts,Category
from accounts.models import Profile

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
      model = Category
      fields = ['id','name']


class PostSerializer(serializers.ModelSerializer):
   
   absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
   
   class Meta:
      model = Posts
      fields = ['author','image','title','content','status','absolute_url','category','created_date','upteted_date','published_date']
      read_only_fields  = ('author',)

   def get_abs_url(self,obj):
      request = self.context.get('request')
      return request.build_absolute_uri(obj.pk)

   def to_representation(self, instance):
       rep= super().to_representation(instance)
       request = self.context.get('request')
       if request.parser_context.get('kwargs').get('pk'):
          rep.pop('created_date',None)
          rep.pop('absolute_url',None)
       else:
          rep.pop('content',None)
            
       rep['category'] = CategorySerializer(instance.category,context={'request':request}).data
       return rep
   
   def create(self, validated_data):
      validated_data['author'] =Profile.objects.get(user__id = self.context.get('request').user.id)
      return super().create(validated_data)