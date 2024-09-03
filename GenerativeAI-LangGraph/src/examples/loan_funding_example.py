from agents.loan_funding_agent import LoanFundingAgent
from langgraph.models import LangGraph

def main():
    # Initialize a LangGraph instance
    lang_graph = LangGraph()

    # Initialize a LoanFundingAgent instance with the LangGraph instance
    loan_funding_agent = LoanFundingAgent(lang_graph)

    # Use the LoanFundingAgent instance to fund a loan
    loan_funding_agent.fund_loan()

if __name__ == "__main__":
    main()