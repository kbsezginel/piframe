import time
import subprocess


class Display:
    def __init__(self):
        self.exec = "vcgencmd"
        self.state = None

    def __repr__(self):
        return f"<Display is {self.state}>"

    def toggle(self, state, check_state=True):
        cmd = [self.exec, "display_power", {"on": "1", "off": "0"}[state]]
        if self.state != state or not check_state:
            self.run(cmd)
            self.state = state
        elif check_state:
            print(f"Display is already {self.state}, cannot turn {state}")

    def display_power(self):
        cmd = [self.exec, "display_power"]
        return self.run(cmd)

    def measure_temp(self):
        cmd = [self.exec, "measure_temp"]
        return self.run(cmd)

    def run(self, cmd, out=True, err=False, verbose=True):
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.stdout.decode(), process.stderr.decode()
        text = ""
        if out:
            text += stdout
        if err:
            text += stderr
        if verbose:
            print(text)
        return text
