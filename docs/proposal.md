# 프로젝트 제안서(Project proposal): "프로젝트 이름(Project name)"

## 1. 프로젝트 주제(Project topic)

### 만들고 싶은 프로그램(What we want to build)

> We will build a Python data processing program that takes an Excel spreadsheet of uncategorized bank transactions. It will automatically classifies each transaction using keyword matching. Then it will saves a new Excel file with a populated "Category" column.


### 사용자 정의 및 해결할 문제(Users and problem)

> Small business owners, accountants, and personal finance managers manually review and categorize hundreds of bank transactions every month. This program automates that repetitive task to save time and reduce manual entry errors.


## 2. 개발할 기능(Planned features)

### 입력(Input)

> The user provides an Excel file containing a month's worth of raw bank transactions stored on their computer. The input file must contain at least Date, Description, and Amount columns.


### 처리(Processing)

> 1. Read the input Excel file into a pandas DataFrame.
> 2. Analyze the Description field against predefined keyword rules.
> 3. Assign matching category names or tag as "Uncategorized" if no match is found.
> 4. Append a new "Category" column to the dataset.
> 5. Export the dataset as a new Excel file.

### 결과(Output)

> The program saves a new Excel file with all original data columns preserved plus a newly populated "Category" column. The original input file remains unchanged.

### 개발 범위(Scope)

> Features to include (in scope):
    - Reading and writing multi-row Excel (.xlsx) files (using pandas and openpyxl)
    - Core keyword-matching based automatic category classification system
    - Add a "Category" Column and Export Results to an Excel File
    - Handling exceptions for unclassified items (assigning the "Uncategorized" tag)
    - Constructing an Excel dataset of mock transaction records for test validation
> Features to exclude (out of scope):
    - Probabilistic reasoning based on machine learning/deep learning
    - Implementation of a Web Interface (Web UI) or Graphical User Interface (GUI)
    - Real-time Bank API Integration
> Limitation: (Undetected or ambiguous transactions may remain as "Uncategorized", so the output Excel file must be reviewed and adjusted manually by the user.)


### 사용 예시(Usage example)

> A user uploads a sample Excel sheet containing diverse transactions, [sample_bank_statement.xlsx] The system automatically tags budget categories like "Food", "Transport", and "Fixed Costs" and outputs [categorized_bank_statement.xlsx]. The user opens the file to verify that the system accurately tags categories and inspects any remaining uncategorized items.
