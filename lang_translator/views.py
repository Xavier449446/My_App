from .serializers import AudioSerializer
from .models import Audio
import os
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .translate import translate
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
import winsound
import pyaudio
import playsound
class AudioCreateView(ModelViewSet):
    queryset=Audio.objects.all()
    serializer_class = AudioSerializer
    def create(self, request, *args, **kwargs):
        if 'audio' not in request.data:
            raise ParseError('No File Uploaded')
        file_obj = request.data['audio']
        path = default_storage.save('media\\', ContentFile(file_obj.read()))
        path= os.path.join(settings.MEDIA_ROOT,path)
        text,voice=translate(path)
        return Response(data=path)