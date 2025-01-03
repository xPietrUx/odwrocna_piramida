import subprocess
import os


def main():
    batch_script = os.path.join("process.bat")

    try:
        print("[PROGRAM.exe]: Skrypt zostal pomyslnie uruchomiony")
        subprocess.run(["cmd.exe", "/c", batch_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[PROGRAM.exe]: Blad podczas uruchomiania skryptu batch: {e}")


if __name__ == "__main__":
    main()
