# ossTeam10-pythonLibrary

## 1. What it does        
Small business owners, accountants, and personal finance managers often spend hours manually sorting through monthly bank statements. This library automates transaction categorization using rule-based keyword matching:

- Reads Bank Statements: Loads zip file containing raw receipt formatted as `.jpg/.png/.pdf`
- Keyword-Based Classification: Matches transaction descriptions against predefined rules to assign budget categories (such as `Food`, `Transport`, and `Fixed Costs`), labeling unmatched entries as `Uncategorized`.
- Non-Destructive Export: Saves a new Excel file with a populated `Category` column
  
## 2. Installation        <- TestPyPI command today, pip install <name> later
- Install the package from TestPyPI (dependencies are installed from PyPI):

```bash
pip install -i https://pypi.org --extra-index-url https://pypi.org receiptsort==0.1.0
```

## 3. Quick start         <- five lines, input file to result
```python
from ossimg.core import grayscale
input_file = "input.png"
output_file = "output.png"
result = grayscale(input_file, output_file)
print(result)
```

## 4. Dependencies        <- your import list, with licenses
1. Pandas
License: BSD 3-Clause 

2. Openpyxl
License: MIT

3. RapidFuzz
License: MIT

4. matplotlib
License: PSF based

5. pyteserract
License: Apache 2.0

6. Teserract OCR
License: Apache 2.0

7. StreamLit
License: Apache 2.0

## 5. Tests               <- TODO (later in this course)
python -m pip install -e . pytest
python -m pytest
## 6. Documentation       <- MkDocs site, API page link
- The project documentation is available on our MkDocs website.
- MkDocssite: https://amierashraf006.github.io/ossTeam10-pythonLibrary
- API page link: https://amierashraf006.github.io/ossTeam10-pythonLibrary/api/

## 7. Release             <- TODO (later in this course)

## 8. Team                
- Team Members & GitHub IDs:
    - Amier Ashraf (@amierashraf006)
    - Farina Nadia (@farinanadiaa)
    - Iman Insyirah (@imaninsyirahsohaimi)
    - Yan Xiyang (@heptapoda)
    - Kim Hyeong-Su (@khs16728)
      
- Team Rules: 
    - Pull request size:
        - One small function(about 100 changed lines)
    - Review process:
        - Reviewer: Everyone aside from author(minimum 2 people)
        - Time limit: within 48 hours after PR
        - What blocks a merge:
          - At least 1 "Request Change" from reviewer Unresolved conversations in the PR comments

    - Merge:
        - Who presses the button: Team leader
        - Merge Option: Merge Commit (Default)
        - Post-Merge Action: Delete the branch immediately after a successful merge
          
    - Conventions & Communication:
        - Branch Naming: feature/feature-name (e.g., feature/login, feature/ai-integration)
        - Commit Message Format: Conventional Commits style
            - feat: ... (adding a feature or functionality)
            - fix: ... (Fixing a bug or error)
            - docs: ... (Updating documentation only)
            - style: ... (Formatting, missing semicolons, or code style changes (no logic change))
            - refactor: ... (Restructuring code without adding a feature or fixing a bug)
            - test: ... (Adding or updating tests) chore: ... (Maintenance tasks, dependency upgrades, or build config updates)
         
- AI usage: Use the disclosure rule from this course
  - AI Usage: AI assistance is utilized for drafting code structures, documentation formatting, and debugging under course guidelines.

## 9. License         
- MIT License. See LICENSE for details.
