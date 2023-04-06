import subprocess

class PreExecCallback:
    def __call__(self):
        raise Exception()

if __name__ == "__main__":
    p = PreExecCallback()