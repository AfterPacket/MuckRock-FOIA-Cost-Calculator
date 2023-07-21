# MuckRock FOIA Cost Calculator

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-GPL%203.0-green.svg)

## Description

The MuckRock FOIA Cost Calculator is a Python script that allows users to calculate the total cost spent on FOIA (Freedom of Information Act) requests for a specified user on the MuckRock platform. The script interacts with the MuckRock API, handling pagination to fetch data from all pages and accurately calculate the total cost spent on FOIA requests.

## Features

- Fetches FOIA request data from the MuckRock API
- Handles pagination to process all pages of data
- Calculates the total cost spent on FOIA requests for a given user
- Converts `price` values to floating-point numbers for accurate calculation

## How to Use

1. Ensure you have Python 3.x installed on your system.

2. Clone this repository to your local machine.

3. Install the required dependencies using pip:

```bash
pip install requests

1.Open the muckrock_foia_cost_calculator.py file in a text editor.

2.Look for the comment # ChangeMe in the code. Replace 'TheJ' with the MuckRock username for which you want to calculate the total cost spent on FOIA requests. Save the file after making the change.

3.Run the script: python muckrock_foia_cost_calculator.py

The script will display the total cost in USD spent on FOIA requests for the specified user.


License
This project is licensed under the GNU General Public License (GPL) version 3.0.

Acknowledgments
This script was developed as part of a personal project to analyze FOIA-related expenses on the MuckRock platform.
The MuckRock API is used to access FOIA request data. Please ensure you comply with their API usage policies.
