# Grocery API

The initial repository for PyLadies Hamburg's "Introduction to FastAPI" workshop.

## Setup

1) Install [python3.8](https://www.python.org/downloads/release/python-3810/)
   * An existing installation of python3.8 or python3.9 should be fine, too.
2) Clone this repository  
   a) In your terminal, execute `git clone http://github.com/paxcodes/grocery_api`  
   b) Still in the terminal, change your working directory: `cd grocery_api`
3) Create the virtual environment
   * Using your python3.8 (or 3.9), run the command `python -m venv --prompt "grocery_api" .venv`
   * ✅ Make sure the `python` command you are using is the 3.8 / 3.9 version.
     * You can check this by running `--version`. E.g.  

        ```sh
        $ python --version
        Python 3.8.10
        ```
      * If it is not the 3.8/3.9 version, try `python3` / `python3.8` instead of `python`. Run `--version` if you are attempting to use `python3` to ensure it's 3.8/3.9.
4) Activate your virtual environment: `source .venv/bin/activate`
   * ✅ Your terminal prompt will be prefixed with `(grocery_api)` once the virtual environment is activated.
   * ✅ Running `which pip` and `which python` should output the `.venv` directory inside your `grocery_api` folder. (e.g. `/grocery_api/.venv/bin/pip` and `/grocery_api/.venv/bin/python`)
   * ✅ Running `python --version` should output 3.8/3.9. If it isn't, see ✅ on Step#3.
5) Install dependencies: `pip install -r requirements.txt`
   * ✅ It should something like, `Successfully installed ... fastapi-0.65.2 ... uvicorn-0.14.0 ... pytest-6.2.4 ... requests-2.25.1`
   * 💡 The requirements.txt is the result when freezing dependencies after installing `fastapi` and `uvicorn`.
6) Run the server: `uvicorn main:app`
   * ✅ It should say,
    ```sh
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    ```
7) Go to your browser and visit, http://127.0.0.1:8000
   * ✅ It should say, `{ "message": "Hello World!" }`
8) Exit the server by pressing `Ctrl+C` in the terminal.
9) Run test: `python -m pytest` 
    * ✅ It should output,
      ```
      ...
      collected 1 item

      tests/test_endpoints.py .     [100%]

      ======== 1 passed in 0.XXs =========
      ```

If you have made it all the way to the end and everything is as expected (✅), you have successfully setup your environment and ready for the workshop!

If you are having trouble with any of the steps, reach out in PyLadies' Slack channel #city-hamburg.
