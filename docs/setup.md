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

### Getting files from GitHub

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

- For example (on macOS), consider hydrostatic pressure file

    `cd tutorials/docs/hydrostatic-pressure/hydrostatic_pressure.py`

1. Run the file.

    `python hydrostatic_pressure.py`

- On Windows, run the file

    `py hydrostatic_pressure.py`

1. The example should print results similar to the following

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/TOKU-Systems/tutorials/develop/docs/pic/Screen%20Shot%202021-09-14%20at%208.01.22%20AM.png">
</p>

## Connection to Database using pandas

1. To connect to the database, install a package called 'psycopg2'

    ```sh
    pip install pyscopg2
    ```

1. Below is an example of running a query to get the latest signal values

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/TOKU-Systems/tutorials/develop/docs/pic/Screen%20Shot%202021-09-14%20at%208.01.22%20AM.png">
</p>

- Line 1 imports the pandas package.
- Line 4-14 is the SQL query to be executed to get collect the required tabled
from the database and the desired results.
- Line 3 enables us to read the query and fetch the results into a dataframe
using pandas.
- Line 15 is the connection to the appropriate database and is constructed as following:
    - `postgresql://` is the scheme which indicates the database technology.
    - `data_viewer` is the user name of the database
    - `tokuapidemosystems` is the password of the database.
    - `apidemo.tokusystems.com` is the database host.
    - `new_mareland` is the name of the target database

- This is specific to the example considered, connection can be made with any
available databases and for any of the above information needed please contact [TOKU-Systems-Help-desk](https://www.tokusystems.com/contact/)

### Optional tools

1. Install [pgadmin](https://www.pgadmin.org/download/)
    - It is a GUI tool used to link (remote and locally) to PostgreSQL database.
        - Select tsdb (working database).
        - Can use it to view tables and write new SQL queries and analyse the results.

1. Install [Visual Studio Code editor](https://code.visualstudio.com/download)
    - It is an editor used to make alterations in the code and modify it.
        - Open tutorials folder.
        - Run the file.
        - View the results in the terminal.
