# Request admin privileges to complete tasks that require them.
import sys
import ctypes

# Ask for admin privileges on Windows
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
# Function to relaunch the app with administrator privileges
def request_admin_privileges():
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit()  # Exit the current instance of the app