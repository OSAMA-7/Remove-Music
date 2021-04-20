#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
    import os
    import requests
    from os import system
    system("title " + "Soud Was Here - @8Y - Soud#5866")
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
logo = f"""
{Fore.CYAN}         _______   __           
{Fore.CYAN}   ____ |  _  \ \ / / 
{Fore.CYAN}  / __ \ \ V / \ V / 
{Fore.CYAN} / / _` |/ _ \  \ / 
{Fore.CYAN}| | (_| | |_| | | | 
{Fore.CYAN} \ \__,_\_____/ \_/ 
{Fore.CYAN}  \____/ 
"""
print(logo)
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
file_name = input("Enter File name (Test.mp3): ")
try:
	data = open(file_name, "rb").read()
	url = f"http://servers.hammel.in:8001/?name={file_name}"
	headers = {
		"Host": "servers.hammel.in:8001",
		"Content-Type": "application/binary",
		"Connection": "keep-alive",
		"Accept": "*/*",
		"User-Agent": "Hammel/2.1 CFNetwork/1206 Darwin/20.1.0",
		"Accept-Language": "en-us",
		"Accept-Encoding": "gzip, deflate"
		}
	req = requests.post(url, data=data, headers=headers, stream=True)
	with open("@8Y.mp3", "wb") as result:
		result.write(req.content)
	print("\n\n[+] Done Removing Music (@8Y.mp3)\n\n")
	input()
	exit()


except Exception as i:
    print("Something Went Wrong\n")
    print(i)
    input()
    exit()
