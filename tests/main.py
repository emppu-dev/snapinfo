from snapinfo import info
import json

def main():
    snapinfo = info.SnapInfo()

    username = input("Snapchat username: ")

    try:
        user_info = snapinfo.get_info(username)

        json_info = json.dumps(user_info, indent=2)
        print("User Information:")
        print(json_info)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()