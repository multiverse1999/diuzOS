import subprocess

def open_multiple_powershell_windows():
    try:
        subprocess.Popen(["start", "powershell"], shell = True)
        print("first powershell window opened")

    except Exception as e:
        print(f"failed to open powershell windows: {e}")

if __name__ == "__main__":
    open_multiple_powershell_windows()
