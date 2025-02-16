import subprocess

def cleanup_disk():
    try:
        # Run Windows Disk Cleanup tool
        subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
        print("Disk cleanup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Disk cleanup failed: {e}")