1)Easiest issues to fix were style and documentation errors reported by Flake8 and Pylint such as missing docstrings and inconsistent spacing.
Hardest issues to fix were the logic,security and maintainability such as the mutable default argos logs=[], unclosed file handlers and un-sanitised input handling. Had to give error handling scenarios and accurate function handlings for these. These required redesigning the code.

2)Yes,reported naming convention warnings such as addItem should be add_item. These warnings were not actual bugs and did not impact the functionality of the code. Another case was the missing module docstring warning.

3)During development the tools can be integrated to the code to run automatically in the IDE/codebase. In CI/CD this can be run in github actions which does the appropriate testing and then can be rectified.

4)Using with open() block file leaks, removing eval() removed a RCE risk, logging replaced raw print calls enabling proper monitoring and debugging.
