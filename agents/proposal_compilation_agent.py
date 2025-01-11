# agents/proposal_compilation_agent.py
def compile_proposal(insights, use_cases, resources):
    """
    Compile the final proposal with industry insights, use cases, and resources.
    """
    proposal = f"""
    ## Industry Insights
    - **Industry**: {insights['industry']}
    - **Key Offerings**: {", ".join(insights['offerings'])}
    - **Focus Areas**: {", ".join(insights['focus_areas'])}
    - **Trends**: {", ".join(insights['trends'])}

    ## Proposed Use Cases
    """
    for case in use_cases:
        proposal += f"\n- **{case['title']}**: {case['description']}"

    proposal += "\n\n## Resources\n### Datasets"
    for dataset in resources["datasets"]:
        proposal += f"\n- [{dataset['use_case']}]({dataset['link']})"

    proposal += "\n\n### Tools"
    for tool in resources["tools"]:
        proposal += f"\n- {tool}"

    return proposal
