import subprocess

class IOManager:
    @staticmethod
    def exec_cmd(cmd):
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        stdout, stderr = out.communicate()
        print()
        if stderr is None:
            print("\n".join(stdout.decode("utf-8").split('\n')))
        else:
            print("\n".join(stderr.decode("utf-8").split('\n')))

