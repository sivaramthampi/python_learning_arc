## data serializing concept is done in this module

from rest_framework.serializers import ModelSerializer
from .models import userprofile

class userserializers(ModelSerializer):
    class Meta:
        model= userprofile
        fields="__all__"   ## its a dunder method used to serialize all fields in userprofile
        