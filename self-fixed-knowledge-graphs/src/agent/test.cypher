// MATCH (keanu:Person {name: 'Keanu Reeves'}) RETURN keanu.name AS name, keanu.born AS born

// MATCH (p:Person) RETURN p LIMIT 5

// MATCH (bornInEighties: Person)-[a:ACTED_IN]->(m: Movie)
// RETURN bornInEighties.name AS name, bornInEighties AS born
// ORDER BY born DESC
// LIMIT 5

// MATCH (m:Movie {title: 'The Matrix'})<-[d:DIRECTED]-(p:Person) RETURN p.name AS director

// MATCH (tom:Person {name: 'Tom Hanks'})-[r]->(m:Movie) RETURN type(r) AS type, m.title AS movie

// MATCH (:Person {name: 'Tom Hanks'})-[r:!ACTED_IN]->(m:Movie) RETURN type(r) AS type, m.title AS movies

// MATCH (tom:Person {name: 'Tom Hanks'})--{2}(colleagues: Person) RETURN DISTINCT colleagues.name AS name, colleagues.born AS bornIn ORDER BY bornIn LIMIT 5

// MATCH (p:Person {name: 'Tom Hanks'})--{1, 4}(colleagues: Person) RETURN DISTINCT colleagues.name AS name, colleagues.born AS bornIn ORDER BY bornIn, name LIMIT 

MATCH p = ALL SHORTEST (:Person {name: 'Keanu Reeves'})--+(:Person {name: "Tom Cruise"}) RETURN count(p) AS pathCount, length(p) AS pathLength