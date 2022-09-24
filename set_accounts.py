from tcfbot.account import Account
from tcfbot.database import Database

tcf_accounts = [
    ('gouirididin@gmail.com', 'didin03082000'),
    ('chabanejugurta13@gmail.com', 'bouira10'),
    ("sarahdahmani1010@gmail.com", "sarahsarah1234"),
    ("lyliane.bahri10@gmail.com", "lila97"),
    ('univthr@gmail.com', 'hanane19'),
    ('hakimabouakil24@gmail.com', 'Bouira2021'),
    ('meriembouakil1@gmail.com', 'Bouira2021'),
    ("bachirberkane92@gmail.com", "leopard006"),
    ("allimsofiane22@gmail.com", "allimsofiane26"),
    ("houalikenza2019@gmail.com", "Bouira10@"),
    ("rozamederbel2@gmail.com", "rozamederbel2"),
    ("feriallounis86@gmail.com", "feriallounis86"),
    ('zizoumouhoub5@gmail.com', 'zizouch1'),
    ("ikfmehdi1296@gmail.com", "12041996"),
    ("ahlm3138@gmail.com", "Canada2021"),
    ("saritta20199@gmail.com", "sarah_123"),
    ("faridatakhebari2021@gmail.com", "Bouira10@")
]

tcf_accounts2 = [
    ('omarziane60@gmail.com', 'omarziane'),
    ("Kacisara1998@gmail.com", "1Perlerare"),
    ("yousraslimani44@gmail.com", "licence2020"),
    ("manelzouai24@gmail.com", "FLUFFYbunny296"),
    ("abdeuyahiaoui@hotmail.fr", "france2020"),
    ("s.boucheraine@ensh.dz", "Fsms0cr*"),
    ('sifounesi@gmail.com', 'Sifou@96'),
    ("rezkihadji95@gmail.com", "poulou2020"),
    ("marylar001@gmail.com", "Txx./53qZXSya"),
    ("fdom9361@gmail.com", "20011974"),
    ("moham10medi@outlook.fr", "azerty123456789")
]

tcf_accounts_dap = [
    ("ayahani961@gmail.com", "nouvellevie"), ("Romouzna@gmail.com", "romaissa010407"),
    ("sadounmazigh50@gmail.com", "mazigh123")
]

tcf_accounts_dap2 = [
("herorachid71@gmail.com", "rachidnur2021"),
    ("aminelfc@protonmail.com", "azertybouira2020"), ("youslar09@gmail.com", "YOUSRA09/")
]


db = Database()
db.drop_tables()
db.create_tables()
db.init_data()

for acc in tcf_accounts2:
    account = Account(email=acc[0],
                      password=acc[1],
                      antenna=1,
                      reserved=0,
                      motivation=1,
                      exam=1)
    db.insert_account(account)

for acc in tcf_accounts_dap2:
    account = Account(email=acc[0],
                      password=acc[1],
                      antenna=1,
                      reserved=0,
                      motivation=1,
                      exam=3)
    db.insert_account(account)

db.commit()
db.close()
