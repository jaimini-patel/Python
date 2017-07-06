#@PydevCodeAnalysisIgnore
import requests
from bs4 import BeautifulSoup
import urllib3

from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


def getjanid(jemail, juuid):
    try:
        r = requests.get(
            'https://test.barcodeservices.ccnag.com/rest/v1/janrainScanner?email=' + jemail + '&handle=&UUID=' + juuid + '&search=Search+Janrain', verify=False)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text,"html.parser")
            # print("uuid: ", soup.find("uuid").string")
            #print("email: ", soup.find('yweather:condition')['temp'])
            #print("email: ", soup.find("email").string)
            januuid = soup.find("uuid").string
            janremail = soup.find("email").string
            janresult = str(januuid) + str(",") + str(janremail)
            #print(" {}".format(janresult))
            file = open("D:\Coke - Freestyle\GitHub_Python\Python\output.txt", "a")
            print(janresult)
            file.write(janresult + "\n")
            file.close()

        else:
            r.raise_for_status()
    except:
        print("hello")
        # return(janresult)
