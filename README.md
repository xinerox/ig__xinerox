---

# Instagram Login Automation Script

This Python script automates the login process for Instagram using a list of passwords stored in a text file. The script attempts to log in with each password until it succeeds or exhausts the list.

## Features

- **Login Automation**: Attempts to log in to Instagram with multiple passwords from a text file.
- **Password Cracking Simulation**: For testing purposes, it tries to match the correct password from a list.
- **Error Handling**: Catches and prints errors that occur during the process.
- **Session Management**: Uses session handling to persist cookies and headers between requests.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- **Python 3.x** or later
- `requests` library for making HTTP requests

You can install the required libraries using `pip`:

```bash
pip install requests
```

## Usage

1. **Prepare the Password List**: Create a text file with a list of possible Instagram passwords, one per line. For example:

   ```
   password123
   1234password
   mysecretpassword
   ```

2. **Run the Script**: Execute the script in the terminal:

   ```bash
   python instagram_login.py
   ```

3. **Provide Input**: When prompted, enter your Instagram username and the path to the passwords file:

   ```
   Enter Instagram username: your_username
   Enter the path to the passwords file: /path/to/passwords.txt
   ```

4. **Output**: The script will attempt to log in with each password in the list. If successful, it will print a success message in green. If login fails, it will print a failure message in red.

   ```
   Attempting login for @your_username with password | password123
   login failed | @your_username | unknown error # failed
   ```

   If the login is successful, it will stop attempting further passwords.

## Code Explanation

- **Instagram Login Function**: `instagram_login(username, password)` sends a POST request to Instagram's login endpoint using the given username and password.
  - The CSRF token is fetched from the login page before attempting the login.
  - The password is passed in an encoded format.

- **Main Logic**: The script reads passwords from a file, attempts to log in with each, and prints whether the login was successful or not.

- **Session Management**: The script uses a session to persist cookies and headers between requests for the login attempts.

## Example

```bash
$ python instagram_login.py
Enter Instagram username: testuser
Enter the path to the passwords file: passwords.txt
Attempting login for @testuser with password | password123
login failed | @testuser | unknown error # failed
Attempting login for @testuser with password | 1234password
login successful | @testuser with password | 1234password # login successful
```

## Error Handling

- **File Not Found**: If the passwords file is not found, it will print an error message.
- **Unexpected Errors**: Any unexpected errors during the execution will be printed to the terminal.

## Disclaimer

This script is intended for educational and testing purposes only. Do not use it to brute force or attempt unauthorized access to accounts. Always respect the terms of service of any platform you interact with.

## Contact

Made by [@XINEROX](https://t.me/XINEROX).  
Feel free to reach out to me on Telegram for support or inquiries: [Contact on Telegram](https://t.me/XINEROX).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---