import time
import subprocess


class Display:
    def __init__(self):
        self.exec = "vcgencmd"

    def toggle(self, state, check_state=True):
        cmd = [self.exec, "display_power", {"on": "1", "off": "0"}[state]]
        if self.state != state or not check_state:
            self.call(cmd)
            self.state = state
        elif check_state:
            print(f"Display is already {self.state}, cannot turn {state}")

    def display_power(self):
        cmd = [self.exec, "display_power"]
        self.call(cmd)

    def measure_temp(self):
        cmd = [self.exec, "measure_temp"]
        self.call(cmd)

    def call(self, cmd, out=True, err=False, verbose=True):
        process = subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.stdout.decode(), process.stderr.decode()
        text = ""
        if out:
            text += out
        if err:
            text += err
        if verbose:
            print(text)
        return text
