from neo4j import GraphDatabase

URI = "neo4j://172.17.0.2:7687"
AUTH = ("neo4j", "keepgoing7")

def connectToNeo4j():
    """
    连接到Neo4j数据库 (Version5)
    """
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        return driver
    
driver = connectToNeo4j()

# Create Two Nodes With Edge
# summary = driver.execute_query(
#     """
#     CREATE (a:Person {name: $name})
#     CREATE (b:Person {name: $friendName})
#     CREATE (a)-[:KNOWS]->(b)
#     """,
#     name="Alice",
#     friendName="David",
#     database_="neo4j"
# ).summary

# print("Created {nodes_created} nodes in {time} ms.".format(
#     nodes_created=summary.counters.nodes_created,
#     time=summary.result_available_after
# ))

# Retrieve all Person nodes who like other Persons
records, summary, keys = driver.execute_query(
    """
    MATCH (person:Person)-[:KNOWS]->(:Person)
    RETURN person.name AS name
    """,
    database_="neo4j"
)

for record in records:
    print(record.data())

print("The Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query,
    records_count=len(records),
    time=summary.result_available_after
))

# To update an entity's infomation in the database, use the Cypher clauses MATH and SET
records, summary, keys = driver.execute_query(
    """
    MATCH (p:Person {name: $name})
    SET p.age = $age
    """,
    name="Alice",
    age=42,
    database_="neo4j"
)
print(f"Query counters: {summary.counters}.")

# To create a new relationship, linking it to two already existing node, use a combination of the Cypher clauses MATCH and CREATE
records, summary, keys = driver.execute_query(
    """
    MATCH (alice:Person {name: $name})
    MATCH (bob:Person {name: $friend})
    CREATE (alice)-[:KNOWS]->(bob)
    """,
    name="Alice",
    friend="Bob",
    database_="neo4j"
)
print(f"Query counters: {summary.counters}.")