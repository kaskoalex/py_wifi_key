import subprocess


def extract_wifi_passwords():
    profiles_data = subprocess.check_output(
        'netsh wlan show profiles').decode('utf-8').split('\n')

    # print(profiles_data)

    # for item in profiles_data:
    # print(item)

    profiles = [i.split(':')[1].strip()
                for i in profiles_data if "Profil für alle Benutzer" in i]
    #en - "All User Profile"
    print(profiles)

    for profile in profiles:
        profile_info = subprocess.check_output(
            f'netsh wlan show profile "{profile}" key=clear').decode('utf-8').split('\n')
        # en, de, ru different
        #
        try:
            password = [i.split(':')[1].strip()
                        for i in profile_info if 'Schlüsselinhalt' in i][0]
        except IndexError:
            password = None

        # print(password)

        print(f' Profile: {profile}\nPassword: {password}\n{"#" *20}')

        with open(file='wifi passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(
                f' Profile: {profile}\n Password: {password}\n{"#" * 20}\n')


def main():
  extract_wifi_passwords()
if __name__ =='__main__':
  main()

