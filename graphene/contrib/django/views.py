from graphql_django_view import GraphQLView as BaseGraphQLView
from graphql_django_view import BatchGraphQLView as BatchBaseGraphQLView


class GraphQLView(BaseGraphQLView):
    graphene_schema = None

    def __init__(self, schema, **kwargs):
        super(GraphQLView, self).__init__(
            graphene_schema=schema,
            schema=schema.schema,
            executor=schema.executor,
            **kwargs
        )


class BatchGraphQLView(BatchBaseGraphQLView):
    graphene_schema = None

    def __init__(self, schema, **kwargs):
        super(BatchGraphQLView, self).__init__(
            graphene_schema=schema,
            schema=schema.schema,
            executor=schema.executor,
            **kwargs
        )
