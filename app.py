import streamlit as st
from agents.industry_research_agent import research_industry
from agents.use_case_generation_agent import generate_use_cases
from agents.resource_collection_agent import collect_resources
from agents.proposal_compilation_agent import compile_proposal

st.title("AI Use Case Generator")

company_name = st.text_input("Enter the company's name:")

if st.button("Generate Use Cases"):
    if not company_name:
        st.error("Please enter a company name.")
    else:
        st.write("**Step 1: Researching the Industry...**")
        insights = research_industry(company_name)
        st.write(insights)

        st.write("**Step 2: Generating Use Cases...**")
        use_cases = generate_use_cases(insights)
        st.write(use_cases)

        st.write("**Step 3: Collecting Resources...**")
        resources = collect_resources(use_cases)
        st.write(resources)

        st.write("**Step 4: Compiling Proposal...**")
        proposal = compile_proposal(insights, use_cases, resources)
        st.markdown(proposal, unsafe_allow_html=True)

