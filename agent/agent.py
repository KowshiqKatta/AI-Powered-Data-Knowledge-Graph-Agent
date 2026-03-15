import duckdb
from openai import OpenAI
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Initialize the Neo4j driver
driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "password")
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

conn = duckdb.connect("analytics.db")

schema = """
Tables:

customers(customer_id, name, region)
orders(order_id, customer_id, product_id, amount)
products(product_id, product_name, category)

Relationships:
orders.customer_id -> customers.customer_id
orders.product_id -> products.product_id
"""

def get_graph_context():
    """Queries Neo4j to get the current schema and business rules."""
    query = """
    MATCH (t:Table)
    OPTIONAL MATCH (t)-[r:CAN_JOIN_WITH]->(t2:Table)
    RETURN t.name as table, t.columns as columns, t.description as desc,
           collect({target: t2.name, key: r.key}) as joins
    """
    context_str = "Dynamic Schema from Knowledge Graph:\n"
    with driver.session() as session:
        results = session.run(query)
        for record in results:
            context_str += f"- Table: {record['table']}, Columns: {record['columns']}\n"
            if record['desc']:
                context_str += f"  Note: {record['desc']}\n"
            for j in record['joins']:
                if j['target']:
                    context_str += f"  Join: {record['table']} joins {j['target']} on {j['key']}\n"
    return context_str

def generate_sql(question):
# Dynamically fetch schema from the graph
    dynamic_schema = get_graph_context()

    prompt = f"""
    You are a Strict SQL analyst.
    
    {dynamic_schema}

    STRICT RULES:
        1. Only use the table names and column names provided in the schema above.
        2. Do NOT assume, invent, or hallucinate any columns (e.g., do not use 'order_date' if it is not listed).
        3. If the user asks for a filter (like '2024') but the column does not exist in the schema, return this EXACT SQL: 
        SELECT 'Error: The required column (date) is missing from the dataset' AS message;
        4. Return ONLY the SQL code.

    Generate SQL to answer: {question}
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    sql = response.choices[0].message.content
    return sql.replace("```sql", "").replace("```", "").strip()

def clean_sql(sql):
    # Remove markdown fences
    sql = sql.replace("```sql", "").replace("```", "").strip()
    # Drop commentary lines like "Note:" or anything not starting with SQL keywords
    sql = "\n".join(
        line for line in sql.splitlines()
        if not line.strip().lower().startswith("note:")
    )
    return sql

def run_query(sql):
    try:
        result = conn.execute(sql).fetchdf()
        return result, None
    except Exception as e:
        return None, str(e)

def get_graph_metadata():
    query = """
    CALL {
      MATCH (n) RETURN count(n) AS nodeCount
    }
    CALL {
      MATCH ()-[r]->() RETURN count(r) AS relCount
    }
    MATCH (n)
    WITH nodeCount, relCount, labels(n) AS labels
    UNWIND labels AS label
    RETURN nodeCount, relCount, collect(distinct label) AS allLabels
    """
    with driver.session() as session:
        result = session.run(query)
        return result.single()

if __name__ == "__main__":

    question = input("Ask a data question: ")

    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)

    result = run_query(sql)

    print("\nResult:")
    print(result)
