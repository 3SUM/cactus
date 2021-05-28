import Account as ac


class Client:
    def __init__(self, account):
        self.account = account

        self.login_url = "https://auth.riotgames.com/api/v1/authorization"
        self.login_session_body = {
            "claims": "",
            "acr_values": "urn:riot:bronze",
            "redirect_uri": "http://localhost/redirect",
            "client_id": "riot-client",
            "nonce": 1,
            "response_type": "token id_token",
            "scope": "openid link ban lol_region",
        }

        self.login_token_body = {
            "type": "auth",
            "language": "em_US",
            "remember": "false",
            "region": self.account.region,
            "username": self.account.username,
            "password": self.account.password,
        }

        self.purchase_info_url = ""
        self.purchase_info_headers = {}

        self.name_check_url = ""
        self.name_check_headers = {}

        self.change_name_url = ""
        self.change_name_body = ""
        self.change_name_referer = ""
        self.change_name_headers = {}

    def Build(self):
        if self.account.region == "NA1":
            self.purchase_info_url = "https://na.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"
            self.name_check_url = f"https://na.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}"
            self.change_name_url = "https://na.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = "https://na.store.leagueoflegends.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion=na2&selectedItems=&page=featured&recipientSummonerId="
        elif self.account.region == "EUN1":
            self.purchase_info_url = "https://eun.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"
            self.name_check_url = f"https://eun.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}"
            self.change_name_url = "https://eun.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = (
                f"https://eun.store.leagueoflegends.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion="
                f"{self.account.region}&selectedItems=&page=featured&recipientSummonerId="
            )
        elif self.account.region == "EUW1":
            self.purchase_info_url = "https://euw.store.leagueoflegends.com/storefront/v3/history/purchase?language=en_GB"
            self.name_check_url = f"https://euw.store.leagueoflegends.com/storefront/v3/summonerNameChange/verify/{self.account.alias}"
            self.change_name_url = "https://euw.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=en_GB"
            self.change_name_referer = (
                f"https://euw.store.leagueoflegends.com/storefront/ui/v1/app.html?language=en_GB&port=52684&clientRegion="
                f"{self.account.region}&selectedItems=&page=featured&recipientSummonerId="
            )

    def UpdateAccountID(self):
        self.change_name_body = '{"summonerName":"'
        self.change_name_body += self.account.alias
        self.change_name_body += '","accountId":'
        self.change_name_body += self.account.account_id
        self.change_name_body += ',"items":[{"inventoryType":"SUMMONER_CUSTOMIZATION","itemId":1,"ipCost":13900,"rpCost":null,"quantity":1}]}'

    def UpdateAccessToken(self):
        self.purchase_info_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token,
        }

        self.name_check_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Authorization": "Bearer " + self.account.access_token,
        }

        self.change_name_headers = {
            "User-Agent": "RiotClient/18.0.0 (lol-store)",
            "Accept": "application/json",
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.account.access_token,
            "Referer": self.change_name_referer,
        }
