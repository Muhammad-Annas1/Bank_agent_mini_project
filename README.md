# Bank Agent Mini Project 

This is a simple **Bank Agent CLI Project** using **Google Gemini 1.5 Flash API**.  
It simulates a bank customer service system with multiple agents such as **Account Agent** and **Loan Agent**.  
The main agent (**Bank Agent**) hands off customer queries to the relevant sub-agent depending on the context.

---

## Features
- Multiple agents (**Bank Agent**, **Account Agent**, **Loan Agent**)
- Proper **input guardrails** (validating user input)
- Proper **output guardrails** (controlling responses)
- **Context-aware** agent handoff
- **Command-line interface (CLI)** based interaction
- Uses **Google Generative AI (Gemini 1.5 Flash)**

---

## Folder Structure
Bank_agent_mini_project/
│── agents_setup.py # All agents setup and configuration
│── main.py # Main CLI program
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Bank_agent_mini_project.git
cd Bank_agent_mini_project

## Installation & Setup
python -m venv venv
Install Dependencies

## Run the program
python main.py

![Bank Agent Output](relative/path/to/Output.png)
