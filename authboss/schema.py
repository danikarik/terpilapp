import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(object):
    users = graphene.List(UserType)
    profiles = graphene.List(ProfileType)
    viewer = graphene.Field(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.select_related('user').all()

    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user
