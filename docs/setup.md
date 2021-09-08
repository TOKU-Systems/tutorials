# Getting started

To try the tutorials yourself, please setup your development environment as follows.

## macOS

To install on macOS, follow these steps

1. Install [Homebrew](https://brew.sh/)

- This acts as a missing package manager for macOS.

1. Install [python3](https://formulae.brew.sh/formula/python@3.9)

1. Setup [pyenv](https://github.com/pyenv/pyenv)

- Lets you alternate between various versions of python.

### Getting files from Git

1. Clone the repository 'tutorials' from [Github](https://github.com/TOKU-Systems/tutorials)

```sh
git clone <repo>
```

- there are three ways to clone a repository,
    - copying HTTPS
    - copying SSH
    - downloading the zip

1. Change the working directory to the path of the file that is to be executed.

- For example, consider hydrostatic pressure file

`cd tutorials/docs/hydrostatic-pressure`

1. Run the file.

`python hydrostatic_pressure .py`

1. view the results.

### To access the documentation

- Follow the steps in the README.md file to open the mkdocs server and view the
documentation on Bitbucket.

### Optional tools

- Install [pgadmin](https://www.pgadmin.org/download/)
    - A GUI tool used to link (remote and locally) to Postgres database
        - Select tsdb (working database)
        - Can use it to view tables and write new SQL queries and analyse the results.

- Install [vscode-editor](https://code.visualstudio.com/download)
    - An editor used to make alterations in the code and modify it.
        - Open tutorials folder
        - create virtual environemnt using.

        ```sh
        python -m venv .venv
        ```

        - Activate the environment.

        ```sh
        source .venv/bin/activate
        ```

        - install the requirements.

        ```sh
        pip install -r requirements.txt
        ```

        - Run the file.

        - View the results in the terminal.
