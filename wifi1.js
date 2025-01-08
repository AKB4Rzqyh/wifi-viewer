import subprocess
import re

def get_wifi_passwords():
    try:
        # Run the command to get saved Wi-Fi profiles
        profiles_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore')
        profiles = re.findall("All User Profile\s*:\s(.*)", profiles_output)

        wifi_credentials = {}
        for profile in profiles:
            # Run the command to get details of each Wi-Fi profile
            profile_info_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile.strip(), 'key=clear']).decode('utf-8', errors='ignore')
            # Extract the password
            password = re.search("Key Content\s*:\s(.*)", profile_info_output)
            wifi_credentials[profile.strip()] = password.group(1) if password else None

        return wifi_credentials

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    passwords = get_wifi_passwords()
    for wifi, password in passwords.items():
        print(f"Wi-Fi: {wifi}, Password: {password if password else 'No password found'}")
