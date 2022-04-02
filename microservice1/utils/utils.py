import os

import requests

RESILIENCE_CODE = "TIMEOUT"


def post_resilience(url, payload):
    try:
        return requests.post(url, json=payload, timeout=int(os.getenv('SERVICE_TIMEOUT')))
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        return RESILIENCE_CODE
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return RESILIENCE_CODE
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return RESILIENCE_CODE
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        return RESILIENCE_CODE


def get_resilience(url):
    try:
        return requests.get(url, timeout=int(os.getenv('SERVICE_TIMEOUT')))
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        return RESILIENCE_CODE
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return RESILIENCE_CODE
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return RESILIENCE_CODE
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        return RESILIENCE_CODE


def delete_resilience(url):
    try:
        return requests.delete(url, timeout=int(os.getenv('SERVICE_TIMEOUT')))
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        return RESILIENCE_CODE
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return RESILIENCE_CODE
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return RESILIENCE_CODE
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        return RESILIENCE_CODE


def check_resilience(code):
    return code == RESILIENCE_CODE


def resilience_message():
    return os.getenv('MESSAGE_TIMEOUT'), 503
