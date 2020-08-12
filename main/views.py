from strawberry.django.views import GraphQLView as BaseGraphQLView

from .schema import Query


class GraphQLView(BaseGraphQLView):
    def get_root_value(self):
        return Query()
