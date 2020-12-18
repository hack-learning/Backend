from rest_framework import serializers
from students.models import studen, technologi, project, courses, week


class studenSerializer(serializers.ModelSerializer):

    class Meta:
        model = studen
        fields = '__all__'

class technologiSerializer(serializers.ModelSerializer):

    class Meta:
        model = technologi
        fields = '__all__'

class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = project
        fields = '__all__'

class weekSerializer(serializers.ModelSerializer):

    class Meta:
        model = week
        fields = '__all__'

class coursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = courses
        fields = '__all__'