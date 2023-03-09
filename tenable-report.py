def list_servers():
    import requests
    from operator import itemgetter
    import os
    from dotenv import load_dotenv

    load_dotenv()
    access_key = os.getenv('ACCESS_KEY')
    secret_key = os.getenv('SECRET_KEY')
    url = 'https://cloud.tenable.com/scans/'
    headers = {"accept": "application/json", "x-apikeys": 'accessKey={};secretKey={}'.format(access_key, secret_key)}
    scan_ids = [
        [370, "integra   ", '5ebadd08-0314-43db-b76f-b4919efcb346'],  # Integra NOVO
        [164, "auto-dev  "],  # SkyOne-AutoSky -Dev
        [112, "portal-cli"],  # SkyOne-PainelCliente
        [408, "sky-simple"],  # Sky.Simple
        [234, "auto-prd  "],  # SkyOne-AutoSky-Prod
        [336, "sec-man   "],  # Security Manager
        [110, "easy-sky  "],  # SkyOne-EasySky 03/11
    ]

    class Bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    total_critical, total_high, total_medium = 0, 0, 0
    print(Bcolors.HEADER + 'Ambiente\tCri\tHig\tMed\tServer' + Bcolors.ENDC)
    for scan in scan_ids:
        response = requests.get(url+str(scan[0]), headers=headers).json()
        hosts = response["hosts"]
        ambiente = scan[1]
        subtotal_critical, subtotal_high, subtotal_medium = 0, 0, 0
        for host in hosts:
            critical, high, medium, hostname = itemgetter('critical', 'high', 'medium', 'hostname')(host)
            print('{}\t{:03d}\t{:03d}\t{:03d}\t{}'.format(ambiente, critical, high, medium, hostname))
            subtotal_critical += critical
            subtotal_high += high
            subtotal_medium += medium
        print(Bcolors.OKBLUE + "SUBTOTAL\t{:03d}".format(subtotal_critical) + "\t{:03d}".format(subtotal_high) +
              "\t{:03d}".format(subtotal_medium) + Bcolors.ENDC)
        total_critical += subtotal_critical
        total_high += subtotal_high
        total_medium += subtotal_medium
    print(Bcolors.HEADER + "TOTAL\t\t{:03d}".format(total_critical) + "\t{:03d}".format(
        total_high) + "\t{:03d}".format(total_medium) + Bcolors.ENDC)


if __name__ == '__main__':
    print('===========================================')
    # import logging
    # logging.basicConfig(level=logging.DEBUG)
    list_servers()
