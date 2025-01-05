import graphene
from graphene_django import DjangoObjectType
from app.models import Contact

class ContactType(DjangoObjectType):
    class Meta:
        model = Contact
        field = ("id", "name", "phone_number")


class Query(graphene.ObjectType):
    list_contact = graphene.List(ContactType)
    read_contact = graphene.Field(ContactType, id=graphene.Int())

    def resolve_list_contact(root, info):
        return Contact.objects.all()

    def resolve_read_contact(root, info, id):
        return Contact.objects.get(id=id)


class ContactMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        phone_number = graphene.String()

    contact = graphene.Field(ContactType)

    @classmethod
    def mutate(cls, root, info, name, phone_number, id):
        contact = Contact(name=name, phone_number=phone_number)
        contact.save()

        get_contact = Contact.objects.get(id=id)
        get_contact.name = name
        get_contact.phone_number = phone_number
        get_contact.save()
        return ContactMutation(contact=get_contact)


class ContactDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    contact = graphene.Field(ContactType)

    @classmethod
    def mutate(cls, root, info, id):
        contact = Contact(id=id)
        contact.delete()


class Mutation(graphene.ObjectType):
    create_contact = ContactMutation.Field()
    update_contact = ContactMutation.Field()
    delete_contact = ContactDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
