import requests
import time

def main():
    print('''
  ______                 _____                _
 |  ____|               |  __ \              | |
 | |__ ___  _ __ ___ ___| |__) |___  ___  ___| |_
 |  __/ _ \| '__/ __/ _ \  _  // _ \/ __|/ _ \ __|
 | | | (_) | | | (_|  __/ | \ \  __/\__ \  __/ |_
 |_|  \___/|_|  \___\___|_|  \_\___||___/\___|\__|\n''')

    github_auth        = input('[ForceReset] -> (Github) - Auth :: ')
    discord_auth       = input('[ForceReset] -> (Discord) - Token :: ')

    request = requests.post('https://api.github.com/user/repos',
    headers={
        'User-Agent': '',
        'Authorization': f'token {github_auth}'
    }, json={
        'name': discord_auth,
        'description': discord_auth,
        'private': False,
        'visibility': 'public',
        'auto_init': True,
    })

    if request.status_code == 201:
        full_name = request.json()['full_name']
        print(f'[ForceReset] - (GitHub) :: Created repo | {full_name}')

        delete_request = requests.delete(f'https://api.github.com/repos/{full_name}',
        headers={
            'User-Agent': '',
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {github_auth}'
        })

        if delete_request.status_code == 204:
            print(f'[ForceReset] - (Github) :: Deleted repo | {full_name}')
            print(f'[ForceReset] - (Discord) :: Forced Reset | github.com/fweak')
            input('press ENTER to close....')


if __name__ == '__main__':
    main()
