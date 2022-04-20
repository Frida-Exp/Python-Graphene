## Full-Stack React, Python and GraphQL

## Table of content

- [Intro / Refresher on GraphQL](#queries-using-graphiql-graphql-compared-to-rest)
- [Intro to Graphene]()


# Refresher on GraphQL

## Queries, Using GraphiQL, GraphQL compared to REST

We use the following APIs [Swapi Rest](https://swapi.co) and [GraphQL](https://graphql.org/swapi-graphql)


<table>
<tr>
<th>Query</th>
<th>Response</th>
</tr>
<tr>
<td>

```gql
{
  allFilms {
    film {
      title
    }
  }
}
```

</td>
<td>

```json
{
  "data": {
    "allFilms": {
      "films": [
        {
          "title": "A New Hope"
        },
        {
          "title": "The Empire Strikes Back"
        },
        {
          "title": "Return of the Jedi"
        }
      ]
    }
  }
}
```

</td>
</tr>
</table>

### Arguments

In GraphQL, every field and nested object can get its own set of arguments, making GraphQL a complete replacement for making multiple API fetches. GraphQL comes with a default set of types `Int`, `Float`, `String`, `Boolean`, `ID`, but a GraphQL server can also declare its own custom types, as long as they can be serialized into your transport format.

<table>
<tr>
<th>Query</th>
<th>Response</th>
</tr>
<tr>
<td>

```gql
{
  film(filmID:"1") {
    title
    director
    vehicleConnection(first:2) {
      vehicles {
        name
        model
      }
    }
  }
}
```

</td>
<td>

```json
{
  "data": {
    "film": {
      "title": "A New Hope",
      "director": "George Lucas",
      "vehicleConnection": {
        "vehicles": [
          {
            "name": "Sand Crawler",
            "model": "Digger Crawler"
          },
          {
            "name": "T-16 skyhopper",
            "model": "T-16 skyhopper"
          }
        ]
      }
    }
  }
}
```

</td>
</tr>
</table>