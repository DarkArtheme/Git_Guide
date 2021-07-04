import subprocess

class IOManager:
    @staticmethod
    def exec_cmd(cmd):
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        if stderr is None:
            print(stdout)
        else:
            print(stderr)

