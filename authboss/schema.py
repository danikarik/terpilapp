import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(object):
    users = graphene.List(UserType)
    viewer = graphene.Field(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user
