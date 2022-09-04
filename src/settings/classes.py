from rest_framework import mixins, viewsets


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    """
    """

    pass
