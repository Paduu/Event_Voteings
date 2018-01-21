from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from voteings.models import Event, Game, Voteing
from voteings.serializers import EventSerializer, GameSerializer, VoteingSerializer, UserSerializer
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-createdDate')
    serializer_class = EventSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-createdDate')
    serializer_class = GameSerializer

class VoteingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows voteings to be viewed or edited.
    """
    queryset = Voteing.objects.all()
    serializer_class = VoteingSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that lists all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserMeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that lists the current logged in user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


