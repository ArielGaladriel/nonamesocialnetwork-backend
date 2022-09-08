from rest_framework import mixins, viewsets


class MixedPermission:
    """
    For choosing a permission for a corresponding action
    """
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CreateRetrieveUpdateDestroy(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                  MixedPermission, viewsets.GenericViewSet):
    """
    CRUD class
    """

    pass
