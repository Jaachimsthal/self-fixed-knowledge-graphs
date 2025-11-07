MATCH path = SHORTEST 1 (:Person {name: 'Alice'})-[:KNOWS]->(:Person)
RETURN path