import strawberry
from django import forms


@strawberry.type
class Person:
    name: str


@strawberry.type
class Machine:
    code: str


MyUnion = strawberry.union("Entity", types=(Person, Machine))


class MyForm(forms.Form):
    foo = forms.CharField(required=True)
