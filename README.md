![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Database](https://img.shields.io/badge/Database-DuckDB-yellow)
![Graph](https://img.shields.io/badge/Knowledge%20Graph-Neo4j-green)
![AI](https://img.shields.io/badge/AI-LLM%20Powered-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# **AI-Powered Data Knowledge Graph Agent**

An AI system that understands your data ecosystem and automatically generates SQL queries to answer analytical questions.

Instead of manually exploring datasets, writing SQL, and understanding schema relationships, users can simply ask questions in natural language and the system will analyze the data graph, generate SQL, execute queries, and return insights automatically.

------

**🌍 The Problem This Project Solves**

Modern organizations operate with massive, complex data ecosystems.

Data lives across:

1. warehouses
2. pipelines
3. analytics layers
4. dashboards
5. metadata systems

Understanding how datasets relate to each other is often difficult even for experienced engineers.

------

**Typical workflow today**:
```text
Business Question
       ↓
Find relevant datasets
       ↓
Understand schema relationships
       ↓
Write SQL queries
       ↓
Validate results
```

This process requires **deep institutional knowledge of the data model**.

------

**❗ Key Challenges**

• Data schemas are complex <br>
• Dataset relationships are not obvious <br>
• Analysts spend significant time writing SQL <br>
• Metadata context is often scattered <br>

As data ecosystems grow, answering simple questions becomes harder.

------

**💡 The Core Idea Behind This Project**

This project explores a **new paradigm for data analytics**:

# Instead of humans learning the data model, the AI agent learns the data model through a knowledge graph.

The system builds a Data Knowledge Graph that captures relationships between datasets.

Examples:

```text
customers
└── orders
    └── products
```
Using this graph, the AI agent can reason about:

• which tables are relevant <br>
• how datasets are connected <br>
• what joins are required <br>

Then it automatically generates and executes SQL.

------

**⚡ What This System Can Do**

✔ Answer analytical questions using natural language <br>
✔ Generate SQL automatically <br>
✔ Understand dataset relationships using a knowledge graph <br>
✔ Execute queries on a local analytics database <br>
✔ Display results through an interactive UI <br>

**Example question**: Which region generated the highest revenue? <br>
**Generated SQL**: <br>
```
SELECT c.region, SUM(o.amount) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.region
ORDER BY total_revenue DESC
LIMIT 1;
```
----

# **🧠 Architecture**

This system combines **three key components**.

```
                 User
                  │
                  ▼
         Natural Language Question
                  │
                  ▼
             AI SQL Agent
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
 Knowledge Graph         DuckDB
   (Neo4j)             (Analytics DB)
       │                     │
       └──────────┬──────────┘
                  ▼
            Generated SQL
                  │
                  ▼
              Query Result
                  │
                  ▼
             Streamlit UI
```

---

# **🔍 How the System Works**

The workflow follows these steps:

**Step 1: User asks a question** <br>
Example: Which region generated the highest revenue?

---

**Step 2: AI Agent analyzes schema**
The system provides the model with:
1. table schemas <br>
2. column definitions <br>
3. dataset relationships <br>

---

**Step 3: Knowledge Graph provides context**
The Neo4j graph contains relationships like:
```
orders → customers
orders → products
```
This helps the AI determine correct joins.

---

**Step 4: SQL is generated** <br>
The LLM produces the SQL query required to answer the question.

---

**Step 5: Query executes in DuckDB** <br>
The query runs against the analytics database.

---

**Step 6: Results are returned** <br>
The Streamlit interface displays the result.

---

**🖥 Example Questions You Can Ask** <br>
Examples supported by the system:
```
Which region generated the highest revenue?
Which customer spent the most money?
Which product generated the highest revenue?
How many orders were placed per region?
Show revenue by region.
```

---

# **🛠 Installation & Setup**

Clone the repository:
```
git clone https://github.com/KowshiqKatta/AI-Powered-Data-Knowledge-Graph-Agent.git
cd AI-Powered-Data-Knowledge-Graph-Agent
```

Install dependencies:
```
pip install -r requirements.txt
```

# **Run the System**

**Step 1: Generate sample data**
```
python create_data.py
```
---
**Step 2: Setup analytics database**
```
python database/setup_duckdb.py
```
---
**Step 3: Build knowledge graph**
```
python graph/build_graph.py
```
---
**Step 4 — Launch the interface**
```
streamlit run app.py
```
**Open browser:**
```
http://localhost:8501
```
You can now ask questions about the data.

----

# **🧰 Tech Stack**

Core technologies used in this project:
```
| Component       | Technology |
| --------------- | ---------- |
| Language        | Python     |
| AI Agent        | OpenAI API |
| Knowledge Graph | Neo4j      |
| Database        | DuckDB     |
| Interface       | Streamlit  |
```
---

# **🚀 Future Improvements**

This project is an experimental prototype exploring AI-driven analytics.

**Planned improvements include**:

**1️⃣ Retrieval Augmented Generation (RAG)** <br>

Integrate documentation and metadata to provide richer context.

---

**2️⃣ MCP Integration** <br>

Use the Model Context Protocol (MCP) to enable structured tool communication between the AI agent and external systems.

---

**3️⃣ Autonomous Query Planning** <br>

Allow the agent to query the knowledge graph dynamically instead of relying on predefined schema prompts.

---

**4️⃣ Cloud Deployment** <br>

Deploy the system to cloud infrastructure so users can access it as a hosted analytics service.

---

**5️⃣ Data Lineage Visualization** <br>

Extend the graph layer to visualize dataset lineage and pipeline dependencies.

---

# **🎯 Why This Project Matters**

This project explores the **future of AI-assisted data analytics**.

Instead of writing SQL manually, engineers and analysts can interact with data systems using **natural language and intelligent agents**.

Such systems have the potential to:
1. accelerate analytics workflows <br>
2. reduce dependence on manual SQL writing <br> 
3. democratize data access across organizations <br>

## Who Can Benefit From This?

This system can be useful for:

• Data analysts exploring unfamiliar datasets <br>
• Data engineers managing complex data models  <br>
• Business users who want quick insights without writing SQL  <br>
• AI researchers exploring agent-based data systems <br>
 
---

**⭐ If You Found This Interesting**

Feel free to fork, improve, and experiment with this project.
