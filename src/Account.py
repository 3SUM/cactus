import enum
import os


class Account:

    Regions = {
        "EUNE": "EUN1",
        "EUW": "EUW1",
        "NA": "NA1"
    }

    def __init__(self):
        self.username = ""
        self.password = ""
        self.alias = ""
        self.region = ""
        self.mode = ""
        self.access_token = ""
        self.account_id = ""
        self.be = 0
        self.rp = 0
        self.name_status = ""
        self.requests_count = 0
        self.days = 0

    def Setup(self):
        self.username = str(input('\t> Username: '))
        if len(self.username) == 0:
            raise Exception('Username expected.')

        self.password = str(input('\t> Password: '))
        if len(self.password) == 0:
            raise Exception('Password expected.')

        self.alias = str(input('\t> Requested name: '))
        if len(self.alias) == 0:
            raise Exception('Name expected.')

        self.region = str(input('\t> Region [Abbreviation]: ')).upper()
        if self.region in self.Regions:
            self.region = self.Regions[self.region]
        else:
            raise Exception('Invalid region.')

        self.mode = str(input('\t> Mode [Turbo/Sniper]: ')).upper()
        if self.mode != "TURBO" and self.mode != "SNIPER":
            raise Exception('Invalid mode.')
