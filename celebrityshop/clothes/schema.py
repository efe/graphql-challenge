import graphene
from graphene_django.types import DjangoObjectType

from celebrityshop.clothes.models import Celebrity, Cloth


class CelebrityType(DjangoObjectType):
    class Meta:
        model = Celebrity


class ClothType(DjangoObjectType):
    class Meta:
        model = Cloth


class Query(graphene.AbstractType):
    # Celebrity
    list_celebrities = graphene.List(CelebrityType,
                                     name=graphene.String(),
                                     age=graphene.Int())

    celebrity = graphene.Field(CelebrityType,
                               name=graphene.String(),
                               age=graphene.Int(),
                               )

    def resolve_list_celebrities(self, info, *args, **kwargs):
        name = kwargs.get('name')
        age = kwargs.get('age')

        qs = Celebrity.objects.all()

        if name is not None:
            qs = Celebrity.objects.filter(name__icontains=name)

        if age is not None:
            qs = Celebrity.objects.filter(age=age)

        return qs

    def resolve_celebrity(self, info, *args, **kwargs):
        name = kwargs.get('name')
        age = kwargs.get('age')

        if name is not None:
            return Celebrity.objects.get(name=name)

        if age is not None:
            return Celebrity.objects.get(age=age)

        return None

    # Cloth
    list_clothes = graphene.List(ClothType,
                                 name=graphene.String(),
                                 price=graphene.Float(),
                                 quantity=graphene.String(),
                                 item_id=graphene.String(),
                                 )

    cloth = graphene.Field(ClothType,
                           item_id=graphene.String(),
                           name=graphene.String(),
                           price=graphene.Float(),
                           quantity=graphene.Int(),
                           )

    def resolve_list_clothes(self, info, *args, **kwargs):
        qs = Cloth.objects.all()

        if info.context.user.is_anonymous():
            qs = qs.filter(visibility=True)

        return qs

    def resolve_cloth(self, info, *args, **kwargs):
        item_id = kwargs.get('item_id')
        name = kwargs.get('name')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        if item_id is not None:
            return Cloth.objects.get(item_id=item_id)

        if name is not None:
            return Cloth.objects.get(name=name)

        if price is not None:
            return Cloth.objects.get(price=price)

        if quantity is not None:
            return Cloth.objects.get(quantity=quantity)

        return None


class CreateCelebrity(graphene.Mutation):
    name = graphene.String()
    age = graphene.Int()

    class Input:
        name = graphene.String()
        age = graphene.Int()

    @staticmethod
    def mutate(root, input, context, info):
        celebrity = Celebrity(
            name=input.get('name'),
            age=input.get('age')
        )
        celebrity.save()

        return CreateCelebrity(
            id=celebrity.id,
            name=celebrity.name,
            age=celebrity.age,
        )


class Mutation(graphene.AbstractType):
    create_celebrity = CreateCelebrity.Field()
