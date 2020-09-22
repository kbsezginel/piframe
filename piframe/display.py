import time
from subprocess import Popen, PIPE


class Display:
    def __init__(self):
        self.exec = "vcgencmd"
        self.state = None

    def __repr__(self):
        return "<Display is %s>" % self.state

    def toggle(self, state, check_state=True):
        cmd = [self.exec, "display_power", {"on": "1", "off": "0"}[state]]
        if self.state != state or not check_state:
            self.run(cmd)
            self.state = state
        elif check_state:
            print("Display is already %s, cannot turn %s" % (self.state, state))

    def display_power(self):
        cmd = [self.exec, "display_power"]
        return self.run(cmd)

    def measure_temp(self):
        cmd = [self.exec, "measure_temp"]
        return self.run(cmd)

    def run(self, cmd, out=True, err=False, verbose=True):
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        rc = p.returncode
        text = ""
        if out:
            text += stdout
        if err:
            text += stderr
        if verbose:
            print(text)
        return text
