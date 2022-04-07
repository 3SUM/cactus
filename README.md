<br>

<p align="center">
<a href="https://github.com/3SUM"><img width="200" src="./logo/cactus.png" alt="Cactus logo"></a>
</p>

<br>

# Cactus

Cactus is a **WIP** League of Legends summoner name turbo/sniper tool.

There are two modes to Cactus:

1. **Turbo**: Will attempt to change your summoner name to the requested one 24/7 until successful.
2. **Sniper**: Will attempt to change your summoner name to the requested one on the expiration date.
To see when a name expires check out [lolnames.gg](https://lolnames.gg/en/).

Please note this is a **WIP** and updates will happen to improve Cactus. As of now *(15/01/2021)*
the `Turbo` mode is essentially fully functional, while the `Sniper` mode has yet to be completed.
If you wish to obtain a highly sought after name, I recommend hosting various instances of Cactus through [AWS](https://aws.amazon.com/) or something similar. I will not offer help with this though as I am busy.

If you have questions or concerns please feel free to contact me here or on **Discord @icantcode#9343**.

## Legal Disclaimer

This tool was strictly developed to demonstrate how straightforward it is to abuse the Riot API.
Please refrain from using Cactus as it is once again developed for educational purposes only. Nevertheless, if you use this, you are doing it at your own risk. You have been warned.

I am not accountable for any of your actions. Please do not misuse this tool.

## Installation & Usage

To use Cactus you will need `Python 3.x` and the [requests](https://requests.readthedocs.io/en/master/)
library beforehand. If you do not have the library installed please use the following command:

```
pip install requests
```

Once the prerequisites are met, you are free to find the source code [here](./src) and run the following command: **NOTE: You will also need [Account.py](./src/Account.py) and [Client.py](./src/Client.py)**

```
python Cactus.py
```

You will be prompted for your Riot account details, as well as the requested summoner name you wish to
obtain and the mode that Cactus will run in. *Note*, the only regions Cactus has access to are the following
`NA, BR, EUW, & EUNE`. 

## Contributors

[Luis Maya Aranda](https://github.com/3SUM) and [Steele Scott](https://github.com/steele123)

## License

&copy; [Luis Maya Aranda](https://github.com/3SUM). All rights reserved.

Licensed under the MIT License.
