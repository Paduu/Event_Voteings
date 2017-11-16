from rest_framework import serializers
from voteings.models import Event,Game,Voteing
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'eventDate', 'description', 'createdDate', 'modifiedDate')

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'createdDate', 'modifiedDate')

class VoteingSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Voteing
        fields = ('id', 'event', 'game', 'createdDate', 'modifiedDate', 'creator')

class UserSerializer(serializers.ModelSerializer):
    voteings = serializers.PrimaryKeyRelatedField(many=True, queryset=Voteing.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_superuser', 'voteings')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

