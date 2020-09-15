import Account as ac
import Client as cl
import requests
import time
import re
from datetime import datetime, timedelta


class Cactus:

    def __init__(self, account, client):
        self.account = account
        self.client = client

    def Run(self):
        if self.account.mode == "TURBO":
            self.Turbo()
            return
        self.Sniper()

    def Sniper(self):
        print(f'[Cactus] {self.account.mode}')
        self.GetCountDown()
        # modify it so that getCountDown becomes the looping condition

    def Turbo(self):
        print(f'[Cactus] {self.account.mode}')
        self.Login()
        self.client.UpdateAccessToken()
        self.PurchaseInformation()
        print(f'[Cactus] {self.account.username} BE: {self.account.be}')
        self.client.UpdateAccountID()
        self.GetSummonerNameChangeAvailable()

        if self.account.name_status:
            print(
                f'[Cactus] Requested name: {self.account.alias} available.')
            if self.ChangeName():
                print('[Cactus] TURBO SUCCESSFUL!')
        else:
            print(
                f'[Cactus] Requested name: {self.account.alias} not available.')
            print('[Cactus] Starting turbo...')
            while True:
                time.sleep(2.4)
                if self.ChangeName():
                    print('[Cactus] TURBO SUCCESSFUL!')
                    break
                else:
                    self.account.requests_count += 1
                    print(f'Requests: {self.account.requests_count}')
                    if self.account.requests_count % 195 == 0:
                        if self.Login():
                            print('[Cactus] NEW ACCESS TOKEN')
                            self.client.UpdateAccessToken()

    def Login(self):
        # Attempt POST request
        response = requests.post(
            self.client.login_url, data=self.client.login_body, headers=self.client.login_headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "access_token" in data:
            print('[Cactus] Login successful!')
            self.account.access_token = data["access_token"]
            return
        else:
            raise Exception('Login Failed.')

    def PurchaseInformation(self):
        # Attempt GET request
        response = requests.get(
            self.client.purchase_info_url, headers=self.client.purchase_info_headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "player" in data:
            self.account.account_id = str(data["player"]["accountId"])
            self.account.be = int(data["player"]["ip"])
            self.account.rp = int(data["player"]["rp"])
            if self.account.be < 13900:
                raise Exception('Not enough BE.')
            return
        else:
            raise Exception('PurchaseInformation failed.')

    def GetSummonerNameChangeAvailable(self):
        # Attempt GET request
        response = requests.get(
            self.client.name_check_url, headers=self.client.name_check_headers)

        # Convert response to JSON
        data = response.json()

        # Verify request worked
        if "nameIsAvailableOnServer" in data:
            self.account.name_status = data["nameIsAvailableOnServer"]
            return
        else:
            raise Exception('GetSummonerNameChangeAvailable failed.')

    def ChangeName(self):
        # Attempt POST request
        response = requests.post(
            self.client.change_name_url, data=self.client.change_name_body, headers=self.client.change_name_headers)

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
    print('[Cactus] Enter Riot account details.')
    print("=" * 60)

    account = ac.Account()
    account.Setup()

    print("=" * 60)

    client = cl.Client(account)
    client.Build()

    vanguard = Cactus(account, client)
    vanguard.Run()
