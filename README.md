# Challenge Project
This is a Django application that provides a GraphQL API for browsing a list of people in an organization.

## Features
- Django app with Person and Address models
- GraphQL API with a people query that supports pagination
- Dockerized application
- Unit tests
- Self-loading sample data

## Setup
Build and run the Docker containers:
`docker-compose up --build`

## Usage
You can interact with the API using the GraphiQL interface at http://localhost:8000/graphql.

Here's an example query:
```
{
  people(pageSize: 2, pageOffset: 1) {
    email
    name
    address {
      number
      street
      city
      state
    }
  }
}
```

## Notes
- Local database is created and loaded with sample data. This sample data will be reloaded during every build for ease of usage

## improvements
- specific configuration for different environments ie. testing, dev, prod
- authentication
- improved database ie. postgres, mongodb
- keyset pagination/cursor pagination to increase performance of database queries
- improve error handling and validation