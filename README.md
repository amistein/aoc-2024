### Getting Started
1. Create your virtual env:
    ```
    python -m venv venv
    ```
1. Run `cp .env-samp .env`
1. Activate you virtual env
    ```
    source venv/bin/activate
    ```
1. Install dependencies
    ```
    pip install -r requirements.txt
    ```
1. To deactivate the virtual env run:
    ```
    deactivate
    ```

### How to download input
1. Log in to AoC with your browser and retreive AoC `session` cookie
1. Copy your `session` cookie to your .env file's `SESSION_COOKIE` variable
    - You'll need to do this each time you login on the AoC website
1. Activate you virtual env
1. Run `python download_input.py DAY [--filepath FILEPATH]`

### Running a solution
- To run your solution functions: `python runner.py [DAY]`

### Adding a solution:
1. Create a new file named `day_[DAY].py` in the `solutions` directory, using one of the previous days as a template
1. In `solutions/__init__.py`, add the new day to the list of imports
1. Once you have the correct solution output, add them to `runner.py` by creating a new `sol[DAY]` variable
