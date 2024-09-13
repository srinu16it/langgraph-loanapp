import unittest
from src.agents.loan_funding_agent import LoanFundingAgent
from src.langgraph.models import LangGraph

class TestLoanFundingAgent(unittest.TestCase):
    def setUp(self):
        lang_graph = LangGraph()
        self.agent = LoanFundingAgent(lang_graph)

    def test_fund_loan(self):
        # Test case for a loan that should be approved
        loan_amount = 10000
        loan_term = 12  # months
        interest_rate = 0.05  # 5% annual interest rate

        result = self.agent.fund_loan(loan_amount, loan_term, interest_rate)
        self.assertTrue(result, "Expected the loan to be approved")

    def test_fund_large_loan(self):
        # Test case for a large loan that might require additional review
        loan_amount = 150000
        loan_term = 36  # months
        interest_rate = 0.04  # 4% annual interest rate

        result = self.agent.fund_loan(loan_amount, loan_term, interest_rate)
        self.assertTrue(result, "Expected the large loan to be approved after review")

    def test_fund_invalid_loan(self):
        # Test case for an invalid loan (negative amount)
        loan_amount = -5000
        loan_term = 12  # months
        interest_rate = 0.05  # 5% annual interest rate

        result = self.agent.fund_loan(loan_amount, loan_term, interest_rate)
        self.assertFalse(result, "Expected the invalid loan to be rejected")

if __name__ == '__main__':
    unittest.main()
