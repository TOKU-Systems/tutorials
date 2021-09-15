# Getting started

To try the tutorials yourself, please setup your development environment as follows.

## macOS

To install on macOS, follow these steps

1. Install [Homebrew](https://brew.sh/)

    - It acts as a package manager for macOS.

1. Using Homebrew, install [python3](https://formulae.brew.sh/formula/python@3.9)

1. Using Homebrew, setup [pyenv](https://github.com/pyenv/pyenv)

    - It enables you alternate between various versions of python.

### Getting files from Git

1. Clone the repository 'tutorials' from [GitHub](https://github.com/TOKU-Systems/tutorials)

    ```sh
    git clone https://github.com/TOKU-Systems/tutorials.git
    ```

    - There are three ways to clone a repository,
        - Copying HTTPS
        - Copying SSH
        - Downloading the zip

1. Change the working directory to the path of the file that is to be executed.

    - For example, consider hydrostatic pressure file

        `cd tutorials/docs/hydrostatic-pressure`

1. Run the file.

    `python hydrostatic_pressure.py`

1. The example should print results similar to the following

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/TOKU-Systems/tutorials/feature/new-changes/docs/pic/Screen%20Shot%202021-09-14%20at%208.01.22%20AM.png">
</p>
### Optional tools

1. Install [pgadmin](https://www.pgadmin.org/download/)
    - It is a GUI tool used to link (remote and locally) to PostgreSQL database
        - Select tsdb (working database)
        - Can use it to view tables and write new SQL queries and analyse the results.

1. Install [Visual Studio Code editor](https://code.visualstudio.com/download)
    - It is an editor used to make alterations in the code and modify it.
        - Open tutorials folder.
        - Create virtual environemnt using

        ```sh
        python -m venv .venv
        ```

        - Activate the environment.

        ```sh
        source .venv/bin/activate
        ```

        - Install the requirements.

        ```sh
        pip install -r requirements.txt
        ```

        - Run the file.

        - View the results in the terminal.
