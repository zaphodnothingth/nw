# set node view limit
:config initialNodeDisplay: 15000

# CREATE NODES
LOAD CSV WITH HEADERS FROM "file:///nodes.csv" as row
WITH row WHERE row.DOI IS NOT NULL
MERGE (c:Article {id: row.DOI, abbrev: coalesce(row.abbrev, 'unkown'), authors:row.auths, title:row.titl, year:row.yr});

----
# CREATE EDGES

LOAD CSV WITH HEADERS FROM "file:///edges.csv" AS row
//look up the two nodes we want to connect up
MATCH (a1:Article {id:row.source}), (a2:Article {id:row.target})
//now create a relationship between them
CREATE (a1)-[:REFERENCES]->(a2);

----
# show all nodes & edges
Match (n)-[r]->(m)
Return n,r,m