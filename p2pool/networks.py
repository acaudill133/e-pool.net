from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    craftcoin=math.Object(
        PARENT=networks.nets['craftcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=3*60*60//15, # shares
        REAL_CHAIN_LENGTH=3*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='74F02D38830612CA'.decode('hex'),
        PREFIX='6D50AAB011632CB1'.decode('hex'),
#        IDENTIFIER='5F08D07F3EB0012D'.decode('hex'),
#        PREFIX='75AD675C0064903B'.decode('hex'),
        P2P_PORT=29903,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8830,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool.e-pool.net crc.xpool.net:12124 p2pool.org:12129 craftcoin.treasurequarry.com:12124 crc.prominer.org:12124 us-east1.cryptovein.com:12124'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    casinocoin=math.Object(
        PARENT=networks.nets['casinocoin'],
        SHARE_PERIOD=5, # seconds target spacing
        CHAIN_LENGTH=3*60*60//5, # shares
        REAL_CHAIN_LENGTH=3*60*60//5, # shares
        TARGET_LOOKBEHIND=60, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='7696C5EF0B281C2F'.decode('hex'),
        PREFIX='4C2E2CD651764B9F'.decode('hex'),
        P2P_PORT=29901,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8840,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net csc.xpool.net:47950 casinocoin.mooo.com:47950 csc-useast.xpool.net:47950 bigiron.homelinux.com:47950 csc.hash.so:3333 csc.squiggie.com:19327'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    catcoin=math.Object(
        PARENT=networks.nets['catcoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='cacacacae0e0e0e0'.decode('hex'),
        PREFIX='fefecfcf0e0f3434'.decode('hex'),
        P2P_PORT=29902,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9993,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool-eu.gotgeeks.com:8333 p2pool-us.gotgeeks.com:8333 rav3n.dtdns.net:8333 doge.dtdns.net:8333 pool.hostv.pl:8333 p2pool.org:8333 p2pool.gotgeeks.com:8333 p2pool.dndns.net:8333 solidpool.org:8333'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    dogecoin=math.Object(
        PARENT=networks.nets['dogecoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='D0D1D2D3B2F68CD9'.decode('hex'),
        PREFIX='D0D3D4D541C11DD9'.decode('hex'),
        P2P_PORT=29905,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9555,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net doge.dtdns.net:8555 p2pool-eu.gotgeeks.com:8555 doge.scryptpool.us:8555 fast-pool.com:8555 primary.dutchdoge.nl:8555 lovok.no-ip.com:8555 doge.lurkmore.com:8555 doge.p2nex.net:8555 doge.crypto49er.com:8555 nogleg.com:8555 doge.jir.dk:8555 dblack.mine.nu:8555 dogepool.glr.com:8555'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    usde=math.Object(
        PARENT=networks.nets['usde'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='1f28fcfe0d56a1a1'.decode('hex'),
        PREFIX='f163e0ac2fe68af2'.decode('hex'),
        P2P_PORT=29948,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8860,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool-eu.gotgeeks.com:8448 p2pool-us.gotgeeks.com:8448 rav3n.dtdns.net:8448 p2pool.gotgeeks.com:8448 p2pool.dndns.net:8448 solidpool.org:8448'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    worldcoin=math.Object(
        PARENT=networks.nets['worldcoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=3*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='793D870E4902D996'.decode('hex'),
        PREFIX='20E8B6037B0F98C7'.decode('hex'),
        P2P_PORT=23620,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8820,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net wdc.xpool.net 148.251.13.168 98.215.74.213 113.105.248.35:44185 198.27.82.133:37420 83.143.34.122:12721 121.101.219.226:50601 216.51.232.156:39594 37.139.8.31:44539 69.197.181.154 14.17.84.30:2503 46.249.46.62 198.58.115.253 162.243.227.221 91.185.199.253:38900 p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dndns.net solidpool.org 198.23.244.216:48907 178.94.109.250:48907 61.144.91.38:48907 173.67.61.119:8541 66.71.246.74:48907 178.94.42.157:48907 37.11.46.125:48907 66.172.10.55:48907 67.189.26.97:48907 178.94.105.190:48907 207.12.89.101:48907 110.174.192.158:48907 93.186.200.124:48907 216.177.81.88:48907 202.104.41.58:48907 76.74.238.175:18122 113.240.247.242:48907 37.11.60.222:48907 199.188.206.150:48907 113.240.247.246:48907 54.229.16.203:48907 78.27.191.182:18122 195.56.77.176:48907 93.186.200.124:18122 128.220.147.219:8541 76.74.238.175:48907 37.11.40.94:48907 173.67.61.119:8535 62.75.216.94:48907 212.48.67.50:8336 97.74.42.79:48907 212.48.67.50:48907 207.12.89.112:48907 78.27.191.182:48907 216.177.81.88:48807 113.243.46.173:48907 66.172.10.55:19331'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    litecoin=math.Object(
        PARENT=networks.nets['litecoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c6923410'.decode('hex'),
        PREFIX='7208c1a53ef629b0'.decode('hex'),
        P2P_PORT=29907,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9327,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net forre.st:9338 vps.forre.st:9338 liteco.in:9338 95.211.21.103:9338 37.229.117.57:9338 66.228.48.21:9338 180.169.60.179:9338 112.84.181.102:9338 74.214.62.115:9338 209.141.46.154:9338 78.27.191.182:9338 66.187.70.88:9338 88.190.223.96:9338 78.47.242.59:9338 158.182.39.43:9338 180.177.114.80:9338 216.230.232.35:9338 94.231.56.87:9338 62.38.194.17:9338 82.67.167.12:9338 183.129.157.220:9338 71.19.240.182:9338 216.177.81.88:9338 109.106.0.130:9338 113.10.168.210:9338 218.22.102.12:9338 85.69.35.7:54396:9338 201.52.162.167:9338 95.66.173.110:8331:9338 109.65.171.93:9338 95.243.237.90:9338 208.68.17.67:9338 87.103.197.163:9338 101.1.25.211:9338 144.76.17.34:9338 209.99.52.72:9338 198.23.245.250:9338 46.151.21.226:9338 66.43.209.193:9338 59.127.188.231:9338 178.194.42.169:9338 85.10.35.90:9338 110.175.53.212:9338 98.232.129.196:9338 116.228.192.46:9338 94.251.42.75:9338 195.216.115.94:9338 24.49.138.81:9338 61.158.7.36:9338 213.168.187.27:9338 37.59.10.166:9338 72.44.88.49:9338 98.221.44.200:9338 178.19.104.251:9338 87.198.219.221:9338 85.237.59.130:9310:9338 218.16.251.86:9338 151.236.11.119:9338 94.23.215.27:9338 60.190.203.228:9338 176.31.208.222:9338 46.163.105.201:9338 198.84.186.74:9338 199.175.50.102:9338 188.142.102.15:9338 202.191.108.46:9338 125.65.108.19:9338 15.185.107.232:9338 108.161.131.248:9338 188.116.33.39:9338 78.142.148.62:9338 69.42.217.130:9338 213.110.14.23:9338 185.10.51.18:9338 74.71.113.207:9338 77.89.41.253:9338 69.171.153.219:9338 58.210.42.10:9338 174.107.165.198:9338 50.53.105.6:9338 116.213.73.50:9338 83.150.90.211:9338 210.28.136.11:9338 86.58.41.122:9338 70.63.34.88:9338 78.155.217.76:9338 68.193.128.182:9338 198.199.73.40:9338 193.6.148.18:9338 188.177.188.189:9338 83.109.6.82:9338 204.10.105.113:9338 64.91.214.180:9338 46.4.74.44:9338 98.234.11.149:9338 71.189.207.226:9338'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-ltc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None,
    ),
    digitalcoin=math.Object(
        PARENT=networks.nets['digitalcoin'],
        SHARE_PERIOD=15, # seconds target spacing
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//15, # shares
        REAL_CHAIN_LENGTH=3*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=45, # blocks
        NEW_SPREAD=45, # blocks
        IDENTIFIER='7696CF5EB2F68C88'.decode('hex'),
        PREFIX='4C2307E841C11FDD'.decode('hex'),
        P2P_PORT=29904,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8810,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool-eu.gotgeeks.com:23610 p2pool-us.gotgeeks.com:23610 rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org dgc.xpool.net dgc.xpool.net:7999 pool.bounceme.net:7999 p2pool.org:7999 dgc.prominer.org:7999 next.afraid.org:7999 108.0.174.26:23610 2.133.128.107:23610 87.209.206.80:23610 162.243.63.239:23610 37.187.46.70:45629 118.127.61.65:23610 144.76.107.81:23610 '.split(' '),
        ANNOUNCE_CHANNEL='#xpool',
        VERSION_CHECK=lambda v: True,
    ),
    zetacoin=math.Object(
        PARENT=networks.nets['zetacoin'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=12*60*60//20, # shares
        REAL_CHAIN_LENGTH=12*60*60//20, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=100, # blocks
        IDENTIFIER='fee2135c7a81bddd'.decode('hex'),
        PREFIX='ccc22f181efcd444'.decode('hex'),
        P2P_PORT=29935,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=8920,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net 146.185.171.176:9174 79.2.130.60:9174 23.253.81.150:9174 p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-zet',
        VERSION_CHECK=lambda v: True,
    ),
    joulecoin=math.Object(
        PARENT=networks.nets['joulecoin'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=10, # blocks
        IDENTIFIER='ac556af4e900ca61'.decode('hex'),
        PREFIX='16ac009e4fa655ac'.decode('hex'),
        P2P_PORT=29947,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=8930,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net rav3n.dtdns.net:7844 bit.usr.sh:7844'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    bitcoin=math.Object(
        PARENT=networks.nets['bitcoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='fc70035c7a81bc6f'.decode('hex'),
        PREFIX='2472ef181efcd37b'.decode('hex'),
        P2P_PORT=29900,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=8800,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net forre.st:9333 vps.forre.st:9333 portals94.ns01.us:9333 54.227.25.14:9333 119.1.96.99:9333 204.10.105.113:9333 76.104.150.248:9333 89.71.151.9:9333 76.114.13.54:9333 72.201.24.106:9333 79.160.2.128:9333 207.244.175.195:9333 168.7.116.243:9333 94.23.215.27:9333 218.54.45.177:9333 5.9.157.150:9333 78.155.217.76:9333 91.154.90.163:9333 173.52.43.124:9333 78.225.49.209:9333 220.135.57.230:9333 169.237.101.193:8335 98.236.74.28:9333 204.19.23.19:9333 98.122.165.84:8338 71.90.88.222:9333 67.168.132.228:9333 193.6.148.18:9333 80.218.174.253:9333 50.43.56.102:9333 68.13.4.106:9333 24.246.31.2:9333 176.31.208.222:9333 1.202.128.218:9333 86.155.135.31:9333 204.237.15.51:9333 5.12.158.126:38007 202.60.68.242:9333 94.19.53.147:9333 65.130.126.82:9333 184.56.21.182:9333 213.112.114.73:9333 218.242.51.246:9333 86.173.200.160:9333 204.15.85.157:9333 37.59.15.50:9333 62.217.124.203:9333 80.87.240.47:9333 198.61.137.12:9333 108.161.134.32:9333 198.154.60.183:10333 71.39.52.34:9335 46.23.72.52:9343 83.143.42.177:9333 192.95.61.149:9333 144.76.17.34:9333 46.65.68.119:9333 188.227.176.66:9336 75.142.155.245:9336 213.67.135.99:9333 76.115.224.177:9333 50.148.193.245:9333 64.53.185.79:9333 80.65.30.137:9333 109.126.14.42:9333 76.84.63.146:9333'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Bitcoin to >=0.8.5!' if v < 80500 else None,
    ),
    asiccoin=math.Object(
        PARENT=networks.nets['asiccoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='2c80035c7a81bc6f'.decode('hex'),
        PREFIX='2472ef181efcd37c'.decode('hex'),
        P2P_PORT=29934,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=8980,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net japool.com:13432 rav3n.dtdns.net:7432 '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-asc',
        VERSION_CHECK=lambda v: True,
    ),
    franko=math.Object(
        PARENT=networks.nets['franko'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='be43F5b8c6924210'.decode('hex'),
        PREFIX='b587192ba6d4729a'.decode('hex'),
        P2P_PORT=29913,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8900,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net us-east1.cryptovein.com:18125 next.afraid.org:18125 coinminer.net 88.161.131.83:29913 37.140.24.83:9639 23.92.27.131:44131 p2pool.org 192.186.133.74:29913 188.227.230.221:29913 162.243.251.98:35141 97.94.98.195:33762 79.2.130.60:11417 113.105.248.35:45651 88.161.131.83:18125 '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    ekrona=math.Object(
        PARENT=networks.nets['ekrona'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=50, # blocks
        IDENTIFIER='fe656b726f6e61fe'.decode('hex'),
        PREFIX='fc656b726f6e61fd'.decode('hex'),
        P2P_PORT=29945,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8950,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool-eu.gotgeeks.com:8344 p2pool-us.gotgeeks.com:8344 rav3n.dtdns.net:8344 taken.pl:8344'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    smartcoin=math.Object(
        PARENT=networks.nets['smartcoin'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=12*60*60//5, # shares
        REAL_CHAIN_LENGTH=12*60*60//5, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='defadefaced0ced0'.decode('hex'),
        PREFIX='d0cededefafac0ce'.decode('hex'),
        P2P_PORT=29983,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8960,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net taken.pl:8585'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    Extremecoin=math.Object(
        PARENT=networks.nets['Extremecoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=3*60*60//15, # shares
        REAL_CHAIN_LENGTH=3*60*60//15, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='5F08D07F3EB0ced0'.decode('hex'),
        PREFIX='75AD675C0064ced0'.decode('hex'),
        P2P_PORT=29966,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8970,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net 192.168.10.101:26666 67.233.200.130'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    potcoin=math.Object(
        PARENT=networks.nets['potcoin'],
        SHARE_PERIOD=15, # seconds target spacing
        NEW_SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=3*60*60//10, # shares
        REAL_CHAIN_LENGTH=3*60*60//10, # shares
        TARGET_LOOKBEHIND=5, # shares coinbase maturity
        SPREAD=10, # blocks
        NEW_SPREAD=10, # blocks
        IDENTIFIER='DDD1A1D3B2F68CDD'.decode('hex'),
        PREFIX='D2C3D4D541C11DDD'.decode('hex'),
        P2P_PORT=29976,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8989,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net xpool.net:8420 us-east1.cryptovein.com:8420 188.226.135.210:8420 '.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    tigercoin=math.Object(
        PARENT=networks.nets['tigercoin'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=12*60*60//5, # shares
        REAL_CHAIN_LENGTH=12*60*60//5, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='b5fafab5dbfdfdd5'.decode('hex'),
        PREFIX='d5fddf5bb5faaffd'.decode('hex'),
        P2P_PORT=29971,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=8938,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net p2pool-eu.gotgeeks.com:8660 p2pool-us.gotgeeks.com:8660 rav3n.dtdns.net:8660 doge.dtdns.net:8660 pool.hostv.pl:8660 p2pool.org:8660 p2pool.gotgeeks.com:8660 p2pool.dtdns.net:8660 solidpool.org:8660 japool.com:8660'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    platinum=math.Object(
        PARENT=networks.nets['platinum'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=24*60*60//5, # shares
        REAL_CHAIN_LENGTH=24*60*60//5, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=100, # blocks
        IDENTIFIER='b5fafab5fab5dfdb'.decode('hex'),
        PREFIX='d5fddffab5dfdbfd'.decode('hex'),
        P2P_PORT=29926,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=8926,
        BOOTSTRAP_ADDRS='p2pool.e-pool.net '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
