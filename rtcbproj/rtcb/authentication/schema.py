import graphene
from graphene_django import DjangoObjectType
from .models import User as UserModel


class ChoicesRoles(graphene.Enum):
    Defender = 'D'
    Striker = 'S'


class User(DjangoObjectType):

    role = ChoicesRoles()

    class Meta:
        model = UserModel
        interfaces = (graphene.Node, )
        exclude_fields = ['password']

    id_db = graphene.ID()

    def resolve_id_db(self, info, **input):
        """ Ritorna  l'ID del db """
        return self.id

    def resolve_password(self, info, **input):
        """ Ritorna  l'ID del db """
        return self.id
    
    def resolve_role(self, info, **kwargs):
        return self.role


