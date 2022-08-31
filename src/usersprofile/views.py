from rest_framework.viewsets import ModelViewSet

from .models import UsersBio, UsersProfile
from .serializers import BioSerializer, ProfileSerializer


class UsersProfileView(ModelViewSet):
    """
    """
    serializer_class = BioSerializer

    def get_queryset(self):
        return UsersBio.objects.filter(user=1)


'''return UsersBio.objects.filter(user_id=int(self.kwargs.get("pk")))'''