import enum
import os


class Account:

    access_token = ""
    accountID = ""
    be = 0
    rp = 0
    nameStatus = ""
    requests = 0
    days = 0

    Regions = {
        "EUNE": "EUN1",
        "EUW": "EUW1",
        "NA": "NA1",
        "BR": "BR1",
        "LAN": "LA1",
        "LAS": "LA2",
        "OCE": "OC1",
        "TR": "TR1",
        "RU": "RU",
        "PBE": "PBE1"
    }

    def __init__(self):
        
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

    
    def Username(self):
        return self.username
    
    def Password(self):
        return self.password

    def Alias(self):
        return self.alias
    
    def Region(self):
        return self.region

    def Mode(self):
        return self.mode