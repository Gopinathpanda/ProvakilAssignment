# ProvakilAssignment
Two csv files are given. one has budget rules and another one has list of investments. Finally, find out the a list of investment opportunities (their IDs, each one on a separate line) which violate the budget.

# Development Setup

## Windows 64 bit

1. Install these tools
    * [Python v3.6.2 64 bit](https://www.python.org/downloads/)
    * [Git](https://git-scm.com/download/win)


1. Upgrade pip

    ```bash
    python -m pip install --upgrade pip
    ```

1. Setup virtualenv

    ```bash
    pip install virtualenv env
    env\ Scripts\ activate
    ```


1. Download backendApp repository

    ```bash
    https://github.com/Gopinathpanda/ProvakilAssignment.git
    ```

1. Install project dependencies

    ```bash
    Go to requirements.txt folder and run command
    pip install -r requirements.txt
    ```
1. Run the Python file

     ```bash
    python InvestmentViolation.py
    ```


