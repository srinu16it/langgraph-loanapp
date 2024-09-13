# Agents Guide

This guide provides an overview of the agents module in the GenerativeAI-LangGraph project.

## Overview

The agents module contains classes that simulate different types of agents. Currently, the module includes a `LoanFundingAgent` class.

## LoanFundingAgent

The `LoanFundingAgent` class simulates an agent that funds loans. It includes methods to evaluate loan applications and decide whether to fund them.

### Usage

Here's an example of how to use the `LoanFundingAgent` class:

```python
from src.agents import LoanFundingAgent

# Initialize the agent
agent = LoanFundingAgent()

# Use the agent to evaluate a loan application
application = {...}  # A dictionary representing a loan application
decision = agent.evaluate(application)

# The decision is a boolean indicating whether the agent decided to fund the loan
print(decision)
```

## Utils

The `utils.py` file in the agents module contains utility functions that are used across the module. These might include functions to process data, calculate metrics, etc.

## Testing

To run tests for the agents module, navigate to the project root directory and run the following command:

```bash
python -m unittest tests/test_agents.py
```
```
This is a basic guide. Depending on the complexity of your project, you might need to provide more detailed instructions, include more examples, or document additional classes and functions.
test