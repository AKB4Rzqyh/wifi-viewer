import subprocess
import re

def get_wifi_password(profile_name):
    try:
        # Run the command to get details of the specific Wi-Fi profile
        profile_info_output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']
        ).decode('utf-8', errors='ignore')
        
        # Extract the password
        password = re.search("Key Content\s*:\s(.*)", profile_info_output)
        return password.group(1) if password else "No password found"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Display all saved profiles
    profiles_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore')
    profiles = re.findall("All User Profile\s*:\s(.*)", profiles_output)

    print("Saved Wi-Fi Profiles:")
    for i, profile in enumerate(profiles, 1):
        print(f"{i}. {profile.strip()}")

    # Ask user to select a Wi-Fi profile
    choice = input("\nEnter the name of the Wi-Fi profile you want to access: ").strip()

    # Retrieve the password for the selected profile
    if choice in profiles:
        password = get_wifi_password(choice)
        print(f"\nWi-Fi: {choice}, Password: {password}")
    else:
        print("\nProfile not found. Please enter a valid profile name.")
