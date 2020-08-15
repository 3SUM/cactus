import Account as ac
import requests
import time
import re
from datetime import datetime, timedelta


class YHLQMDLG:

    def __init__(self, account):
        self.account = account

    def Run(self):
        if self.account.mode == "TURBO":
            self.Turbo()
        self.Sniper()
    
    def Sniper(self):
        print(f'[YHLQMDLG] {self.account.mode}')
        self.GetCountDown()
        # modify it so that getCountDown becomes the looping condition

    def Turbo(self):
        print(f'[YHLQMDLG] {self.account.mode}')
        self.Login()
        self.PurchaseInformation()
        self.GetSummonerNameChangeAvailable()

        if self.account.nameStatus:
            print(
                f'[YHLQMDLG] Requested name: {self.account.alias} available.')
            self.ChangeName()
        else:
            print(
                f'[YHLQMDLG] Requested name: {self.account.alias} not available.')
            print('[YHLQMDLG] Starting turbo...')
            while True:
                time.sleep(2.4)
                if self.ChangeName():
                    print('TURBO SUCCESSFUL!')
                    break
                else:
                    self.account.request += 1
                    print(f'Requests: {self.account.requests}')
                    if self.account.requests % 195 == 0:
                        if self.Login():
                            print('[YHLQMDLG] NEW ACCOUNT TOKEN')

    def Login(self):
        # url
        url = "https://auth.riotgames.com/token"

        # Request body
        body = "client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJodHRwczpcL1wvYXV0aC5yaW90Z2FtZXMuY29tXC90b2tlbiIsInN1YiI6ImxvbCIsImlzcyI6ImxvbCIsImV4cCI6MTYwMTE1MTIxNCwiaWF0IjoxNTM4MDc5MjE0LCJqdGkiOiIwYzY3OThmNi05YTgyLTQwY2ItOWViOC1lZTY5NjJhOGUyZDcifQ.dfPcFQr4VTZpv8yl1IDKWZz06yy049ANaLt-AKoQ53GpJrdITU3iEUcdfibAh1qFEpvVqWFaUAKbVIxQotT1QvYBgo_bohJkAPJnZa5v0-vHaXysyOHqB9dXrL6CKdn_QtoxjH2k58ZgxGeW6Xsd0kljjDiD4Z0CRR_FW8OVdFoUYh31SX0HidOs1BLBOp6GnJTWh--dcptgJ1ixUBjoXWC1cgEWYfV00-DNsTwer0UI4YN2TDmmSifAtWou3lMbqmiQIsIHaRuDlcZbNEv_b6XuzUhi_lRzYCwE4IKSR-AwX_8mLNBLTVb8QzIJCPR-MGaPL8hKPdprgjxT0m96gw&grant_type=password&username="
        body += self.account.region
        body += "%7C"
        body += self.account.username
        body += "&password="
        body += self.account.password
        body += "&scope=openid%20offline_access%20lol%20ban%20profile%20email%20phone"

        # Request headers
        headers = {
            "User-Agent": "RiotClient/17.1.0 (rso-auth)",
            "Accept": "*/*",
            "Content-type": "application/x-www-form-urlencoded"
        }

        # Attempt POST request
        response = requests.post(url, data=body, headers=headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "access_token" in data:
            print('[YHLQMDLG] Login successful!')
            self.account.access_token = data["access_token"]
            return
        else:
            raise Exception('Login Failed.')

    def PurchaseInformation(self):
        # url
        if self.account.region == "NA1":
            url = "https://store.na2.lol.riotgames.com/storefront/v3/history/purchase?language=en_GB"
        else:
            url = "https://store." + self.account.region + \
                ".lol.riotgames.com/storefront/v3/history/purchase?language=en_GB"

        # Request headers
        headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token
        }

        # Attempt GET request
        response = requests.get(url, headers=headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "player" in data:
            self.account.accountID = str(data["player"]["accountId"])
            self.account.be = int(data["player"]["ip"])
            self.account.rp = int(data["player"]["rp"])
            if self.account.be < 13900:
                raise Exception('Not enough BE.')
            return
        else:
            raise Exception('PurchaseInformation failed.')

    def GetSummonerNameChangeAvailable(self):
        # url
        if self.account.region == "NA1":
            url = "https://store.na2.lol.riotgames.com/storefront/v3/summonerNameChange/verify/" + \
                self.account.alias
        else:
            url = "https://store." + self.account.region + ".lol.riotgames.com/storefront/v3/summonerNameChange/verify/" + \
                self.account.alias

        # Request headers
        headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token
        }

        # Attempt GET request
        response = requests.get(url, headers=headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "nameIsAvailableOnServer" in data:
            self.account.nameStatus = data["nameIsAvailableOnServer"]
            return
        else:
            raise Exception('GetSummonerNameChangeAvailable failed.')

    def ChangeName(self):
        url, ref = "", ""
        if self.account.region == "NA1":
            url = "https://store.na2.lol.riotgames.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            ref = "https://store.na2.lol.riotgames.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion=na2&selectedItems=&page=featured&recipientSummonerId="
        else:
            url = "https://store." + self.account.region + \
                ".lol.riotgames.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            ref = "https://store." + self.account.region + ".lol.riotgames.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion=" + \
                self.account.region + "&selectedItems=&page=featured&recipientSummonerId="

        # Request body
        body = "{\"summonerName\":\""
        body += self.account.alias
        body += "\",\"accountId\":"
        body += self.account.accountID
        body += ",\"items\":[{\"inventoryType\":\"SUMMONER_CUSTOMIZATION\",\"itemId\":1,\"ipCost\":13900,\"rpCost\":null,\"quantity\":1}]}"

        # Request headers
        headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.account.access_token,
            "Referer": ref
        }

        # Attempt POST request
        response = requests.post(url, data=body, headers=headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "transactions" in data:
            return True

        return False

    def GetCountDown(self):
        # url
        url = "https://lolnames.gg/en/na/" + self.account.alias

        # Request headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

        # Attempt GET request
        response = requests.get(url, headers=headers)

        # Get days from response
        reg_exp = re.search("available in([^.]*)days.</h4>", response.text)
        days = int(reg_exp.group(1))
        self.account.days = days

        now = datetime.now()
        print("Today's date: " + str(now))

        future_date = now + \
            timedelta(days=self.account.days) + timedelta(hours=16)
        second_date = datetime(
            future_date.year, future_date.month, future_date.day, 16, 0)
        print("Date after: " + str(second_date))

        difference = future_date - now

        # if time has reached, return false so looping stops
        if difference.total_seconds() <= 0:
            return False

        # if time has not been reached, looping condition stays true
        return True


if __name__ == '__main__':
    print('[YHLQMDLG] Enter Riot account details.')
    account = ac.Account()
    account.Setup()
    yh = YHLQMDLG(account)
    yh.Run()
