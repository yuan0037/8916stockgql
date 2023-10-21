from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne import snake_case_fallback_resolvers, load_schema_from_path, ObjectType
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from api.queries import get_stock_resolver, get_stocks_resolver
from api.mutations import add_stock_resolver
from models.stock import Stock


# Defines the execution type that wishes to be done. In this case we defined a Query type inside schema.graphql.
# This will allow us to tie a resolver to a method within the schema.graphql file.
query = ObjectType("Query")

# Allows us to use the functions under the Mutation type that is defined inside of schema.graphql.
mutation = ObjectType("Mutation")

# Binds the keyword that users will invoke to the respective function that is defined from the API perspective.
query.set_field("getStock", get_stock_resolver)
query.set_field("getStocks", get_stocks_resolver)
mutation.set_field("addStock", add_stock_resolver)

# Loads the path to the schema file. Since it's in the same directory, we can simply just input the name.
type_defs = load_schema_from_path("schema.graphql")

# Takes all the information we defined and allows it to be executed when invoked.
schema = make_executable_schema(
	type_defs, query, mutation, snake_case_fallback_resolvers
)


app = Flask(__name__)

# Retrieve HTML for the GraphiQL.
# If explorer implements logic dependant on current request,
# change the html(None) call to the html(request)
# and move this line to the graphql_explorer function.
explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    # On GET request serve the GraphQL explorer.
    # You don't have to provide the explorer if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL explorer app.
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)