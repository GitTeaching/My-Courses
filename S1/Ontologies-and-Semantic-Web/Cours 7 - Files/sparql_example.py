from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://fr.dbpedia.org/sparql")
# sparql = SPARQLWrapper("http://localhost:3030/Cours4Demo/sparql")

sparql.setQuery("""
    PREFIX  dbr: <http://fr.dbpedia.org/resource/>
    PREFIX  dbo: <http://dbpedia.org/ontology/>    

    SELECT DISTINCT ?phils 
    WHERE {
    ?phils  dbo:influenced  dbr:Bernard_Stiegler .
}

""")

sparql.setReturnFormat(JSON)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r['phils']['value'])
except Exception as e:
    print(e)