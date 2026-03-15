import streamlit as st
from agent.agent import generate_sql, run_query, clean_sql, get_graph_metadata

st.title("AI Data Knowledge Graph Agent")

question = st.text_input("Ask a question about the data")

if question:
    sql = generate_sql(question)
    sql = clean_sql(sql)
    st.subheader("Generated SQL")
    st.code(sql, language="sql")
    result, error = run_query(sql)
    if error:
        st.error(error)
    else:
        st.dataframe(result)

st.sidebar.title("Graph Metadata")
if st.sidebar.button("Refresh Metadata"):
    meta = get_graph_metadata()
    if meta:
        st.sidebar.metric("Total Nodes", meta["nodeCount"])
        st.sidebar.metric("Total Relationships", meta["relCount"])
        st.sidebar.write("**Labels found:**")
        for label in meta["allLabels"]:
            st.sidebar.markdown(f"- {label}")
    else:
        st.sidebar.warning("Graph is empty. Run build_graph.py first!")

