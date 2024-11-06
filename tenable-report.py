import json
import os
from operator import itemgetter

import requests
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv("ACCESS_KEY")
secret_key = os.getenv("SECRET_KEY")
headers = {
    "accept": "application/json",
    "x-apikeys": "accessKey={};secretKey={}".format(access_key, secret_key),
}


def print_json_response(url):
    response = requests.get(url, headers=headers)
    print(json.dumps(response.json(), indent=4))


def list_templates():
    # print_json_response("https://cloud.tenable.com/was/v2/templates")
    print_json_response("https://cloud.tenable.com/editor/scan/templates")


def list_folders():
    print_json_response("https://cloud.tenable.com/folders")


def list_servers():
    url = "https://cloud.tenable.com/scans/"
    scan_ids = [
        [45, "Theraskin "],
    ]

    class Bcolors:
        HEADER = "\033[95m"
        OKBLUE = "\033[94m"
        OKCYAN = "\033[96m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"

    total_critical, total_high, total_medium = 0, 0, 0
    print(Bcolors.HEADER + "Ambiente\tCri\tHig\tMed\tServer" + Bcolors.ENDC)
    for scan in scan_ids:
        response = requests.get(url + str(scan[0]), headers=headers).json()
        hosts = response["hosts"]
        ambiente = scan[1]
        subtotal_critical, subtotal_high, subtotal_medium = 0, 0, 0
        for host in hosts:
            critical, high, medium, hostname = itemgetter(
                "critical", "high", "medium", "hostname"
            )(host)
            print(
                "{}\t{:03d}\t{:03d}\t{:03d}\t{}".format(
                    ambiente, critical, high, medium, hostname
                )
            )
            subtotal_critical += critical
            subtotal_high += high
            subtotal_medium += medium
        print(
            Bcolors.OKBLUE
            + "SUBTOTAL\t{:03d}".format(subtotal_critical)
            + "\t{:03d}".format(subtotal_high)
            + "\t{:03d}".format(subtotal_medium)
            + Bcolors.ENDC
        )
        total_critical += subtotal_critical
        total_high += subtotal_high
        total_medium += subtotal_medium
    print(
        Bcolors.HEADER
        + "TOTAL\t\t{:03d}".format(total_critical)
        + "\t{:03d}".format(total_high)
        + "\t{:03d}".format(total_medium)
        + Bcolors.ENDC
    )


if __name__ == "__main__":
    print("===========================================")
    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    list_servers()
    # list_folders()
    # list_templates()
