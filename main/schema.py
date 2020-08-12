import strawberry
import typing
import datetime
import django

from polls.models import Question

User = django.contrib.auth.get_user_model()


@strawberry.type
class QuestionType:
    question_text: str
    pub_date: datetime.datetime

    @strawberry.field
    def created_by(root: "QuestionType") -> "UserType":
        return User.objects.get(id=root.created_by_id)


@strawberry.type
class UserType:
    username: str
    email: str

    @strawberry.field
    def questions(root: "UserType") -> typing.List[QuestionType]:
        return Question.objects.filter(created_by=root)


@strawberry.type
class Query:
    hello: str = "world"

    @strawberry.field
    def users() -> typing.List[UserType]:
        return User.objects.all()


schema = strawberry.Schema(query=Query())
