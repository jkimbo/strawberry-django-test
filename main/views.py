import logging
from strawberry.django.views import GraphQLView as BaseGraphQLView
from graphql.errors import GraphQLError

from .schema import Query

logger = logging.getLogger(__name__)


class GraphQLView(BaseGraphQLView):
    def get_root_value(self):
        return Query()

    def process_errors(self, errors):
        for error in errors:
            try:
                if isinstance(error, GraphQLError) and error.original_error:
                    raise error.original_error
                else:
                    raise error
            except Exception as error:
                logger.exception(error)
