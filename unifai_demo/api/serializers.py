from rest_framework import serializers

from .models import File, Job
from .tasks import del_words


class FileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = File
        # fields =  ['url', 'file', 'name']
        fields = ['url', 'file', 'name', 'filesize', 'content_type']
        read_only_fields =['filesize', 'name', 'content_type']

    def create(self, validated_data):
        f = validated_data['file']
        validated_data['filesize'] = f.size
        validated_data['name'] = f.name
        validated_data['content_type'] = f.content_type

        return super().create(validated_data)


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ['url', 'file', 'freq', 'status', 'result']
        read_only_fields = ['status', 'result']

    def create(self, validated_data):
        ret = super().create(validated_data)
        del_words.delay(ret.id)
        return ret





        