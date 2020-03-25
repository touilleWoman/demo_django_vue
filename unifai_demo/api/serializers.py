from rest_framework import serializers

from .models import File, Job
from .tasks import del_words


class FileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = File
        # fields =  ['url', 'file', 'name']
        fields = ['url', 'file', 'name', 'filesize']
        read_only_fields =['filesize']

    def create(self, validated_data):
        validated_data['filesize'] = validated_data['file'].size
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





        