# Getting started

To try the tutorials yourself, please setup your development environment as follows.

## macOS

To install on macOS, follow these steps

1. Install [Homebrew](https://brew.sh/)

    - It acts as a package manager for macOS.

1. Using Homebrew, install [python3](https://formulae.brew.sh/formula/python@3.9)

1. Check if Git is already installed on the mac [Check-Git-installation](https://github.com/git-guides/install-git)

    - If it is not installed, use Homebrew to
    install [Git](https://www.atlassian.com/git/tutorials/install-git)

1. Using Homebrew, setup [pyenv](https://github.com/pyenv/pyenv)

    - It enables you alternate between various versions of python.

## Windows

To install on Windows, follow these steps

1. Install [python](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)

1. Setup [pyenv-win](https://github.com/pyenv-win/pyenv-win)

## Getting files from GitHub

1. Clone the repository 'tutorials' from [GitHub](https://github.com/TOKU-Systems/tutorials)

    ```sh
    git clone https://github.com/TOKU-Systems/tutorials.git
    ```

    - There are three ways to clone a repository,
        - Copying HTTPS
        - Copying SSH
        - Downloading the zip

1. Change the working directory to the `tutorials` folder.

1. Create a virtual environment.

    ```sh
    python -m venv .venv
    ```

1. Activate the environment.

    ```sh
    source .venv/bin/activate
    ```

1. Install the requirements.

    ```sh
    pip install -r requirements.txt
    ```

1. Navigate to the file that is to be executed.

    - For example, consider hydrostatic pressure file

        `cd tutorials/docs/hydrostatic-pressure/hydrostatic_pressure.py`

1. On macOS, run the file using

    ```sh
        python hydrostatic_pressure.py
    ```

    - On Windows, run the file using

        ```sh
            py hydrostatic_pressure.py
        ```

1. The example should print results similar to the following

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/TOKU-Systems/tutorials/develop/docs/pic/Screen%20Shot%202021-09-14%20at%208.01.22%20AM.png">
</p>

## Using pandas with database

1. To connect to the database, install a package called [pyscopg2](https://www.psycopg.org/docs/)

    ```sh
    pip install pyscopg2
    ```

- Refer to the [pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)

- Follow the instructions below to build the connection URL

1. In order to setup a connection we need the username/password of the database and construct it. For example, consider the conection URL

    `postgresql://data_viewer:tokuapidemosystems@apidemo.tokusystems.com/new_mareland`

1. The connection URL consists of:

    - `postgresql://` is the scheme which indicates the database technology.
    - `data_viewer` is the user name of the database.
    - `tokuapidemosystems` is the password of the database.
    - `apidemo.tokusystems.com` is the database host.
    - `new_mareland` is the name of the target database.

- Report any issues to [GitHub Repo](https://github.com/TOKU-Systems/tutorials/issues)

- Refer to the [ER Diagram](https://illumass-sdk.readthedocs.io/en/develop/api-sql/er-diagram/)

## Optional tools

1. Install [pgadmin](https://www.pgadmin.org/download/)
    - It is a GUI tool used to link (remote and locally) to PostgreSQL database.
        - Select tsdb (working database).
        - Can use it to view tables and write new SQL queries and analyse the results.

1. Install [Visual Studio Code editor](https://code.visualstudio.com/download)
    - It is an editor used to make alterations in the code and modify it.
        - Open tutorials folder.
        - Run the file.
        - View the results in the terminal.
