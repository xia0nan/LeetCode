# LeetCode Solutions

This repository contains my solutions to various LeetCode problems, organized by problem number.

## Problems

| # | Title | Difficulty | Solution | LeetCode Link |
|---|-------|------------|----------|--------------|
| 001 | Two Sum | Easy | [Python](./001_Two_Sum.py) | [Problem](https://leetcode.com/problems/two-sum/) |
| 002 | Add Two Numbers | Medium | [Python](./002_Add_Two_Numbers.py) | [Problem](https://leetcode.com/problems/add-two-numbers/) |
| 003 | Longest Substring Without Repeating Characters | Medium | [Python](./003_Longest_Substring_Without_Repeating_Characters.py) | [Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 004 | Median of Two Sorted Arrays | Hard | [Python](./004_Median_of_Two_Sorted_Arrays.py) | [Problem](https://leetcode.com/problems/median-of-two-sorted-arrays/) |
| 005 | Longest Palindromic Substring | Medium | [Python](./005_Longest_Palindromic_Substring.py) | [Problem](https://leetcode.com/problems/longest-palindromic-substring/) |
| 006 | Zigzag Conversion | Medium | [Python](./006_Zigzag_Conversion.py) | [Problem](https://leetcode.com/problems/zigzag-conversion/) |
| 007 | Reverse Integer | Medium | [Python](./007_Reverse_Integer.py) | [Problem](https://leetcode.com/problems/reverse-integer/) |
| 008 | String to Integer (atoi) | Medium | [Python](./008_String_to_Integer_atoi.py) | [Problem](https://leetcode.com/problems/string-to-integer-atoi/) |
| 009 | Palindrome Number | Easy | [Python](./009_Palindrome_Number.py) | [Problem](https://leetcode.com/problems/palindrome-number/) |

## Environment Setup

### Prerequisites
- Python 3.8+ (Install from [python.org](https://www.python.org/downloads/) or Microsoft Store)
- pip (Python package installer, included with Python)
- Visual Studio Code (recommended)

### Setup Instructions for Windows

#### 1. Install Python
Install Python from the [official website](https://www.python.org/downloads/) or the Microsoft Store.

#### 2. Verify Installation
Open Command Prompt and verify Python is installed:
```
python --version
pip --version
```

#### 3. Clone this repository:
```
git clone https://github.com/yourusername/LeetCode.git
cd LeetCode
```

#### 4. Set up a virtual environment

Using Command Prompt:
```
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate

# Confirm you're using the virtual environment Python
where python
```

Using PowerShell:
```
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate.ps1

# If you get an execution policy error, you might need to run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Using Visual Studio Code:
- Open the project folder in VS Code
- Press Ctrl+Shift+P to open the command palette
- Type "Python: Select Interpreter" and select the virtual environment
- Open a new terminal (it will automatically activate the environment)

#### 5. Install dependencies:
```
pip install pytest
```

#### 6. Deactivate the virtual environment when done:
```
deactivate
```

## Running Tests

Each solution has a corresponding test file in the `test` directory. To run tests:

### Run all tests:
```
pytest
```

### Run tests for a specific problem:
```
pytest test/test_001.py
```

### Run tests with detailed output:
```
pytest -v
```

### Run tests and display print statements:
```
pytest -s
```

## Test File Structure

Test files follow this format:
```python
# test/test_001.py
import pytest
import sys
import os
import importlib

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the solution
solution_module = importlib.import_module("001_two_sum")
Solution = solution_module.Solution

class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()
    
    def test_example_1(self):
        assert self.solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
```

## Resources

For each problem, you can find discussions and alternative approaches on the LeetCode discussion page, linked in the table above.

## Notes

- Solutions are primarily written in Python
- Each solution includes comments explaining the approach and time/space complexity
- All solutions pass LeetCode's test cases

