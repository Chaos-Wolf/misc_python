from datetime import date
today = date.today()
bce = date.fromisoformat('2012-12-21')
total_days = 1872000+abs(today-bce).days
print(total_days)
baktun = total_days//144000
baktun_re = total_days%144000
katun = baktun_re//7200
katun_re = baktun_re%7200
tun = katun_re//360
tun_re = katun_re%360
uinal = tun_re//20
kin = tun_re%20
print(baktun,".",katun,".",tun,".",uinal,".",kin)