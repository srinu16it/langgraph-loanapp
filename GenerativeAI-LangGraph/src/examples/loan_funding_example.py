from agents.loan_funding_agent import LoanFundingAgent
from langgraph.models import LangGraph

def main():
    # Initialize a LangGraph instance
    lang_graph = LangGraph()

    # Initialize a LoanFundingAgent instance with the LangGraph instance
    loan_funding_agent = LoanFundingAgent(lang_graph)

    # Example loan details
    loan_amount = 10000
    loan_term = 12  # months
    interest_rate = 0.05  # 5% annual interest rate

    # Use the LoanFundingAgent instance to fund a loan
    funded = loan_funding_agent.fund_loan(loan_amount, loan_term, interest_rate)

    if funded:
        print(f"Loan of ${loan_amount} successfully funded for {loan_term} months at {interest_rate*100}% interest.")
    else:
        print("Loan funding unsuccessful.")

if __name__ == "__main__":
    main()