class MineCraftServer:
    players = "101"
    tps = "20"
    ping = "111"

    def __init__(self, nickname, ping):
        self.nickname = nickname
        self.ping = ping

st1 = MineCraftServer(nickname="Zelenskyi", ping=1991)
st3 = MineCraftServer(nickname="Zalujniy", ping=993)
st4 = MineCraftServer(nickname="Vova", ping=123)
print(st1, st3, st4)

class WebSite:
    visitors = "10"
    reg_users = "3"
    files = "12"

    def __init__(self, login, password):
        self.login = login
        self.password = password

st2 = WebSite(login="GalyaOtmena", password=12345678)
st5 = WebSite(login="ShtanyZa40UAH", password=98765421)
st6 = WebSite(login="pon", password=345678)
print(st2, st5, st6)


