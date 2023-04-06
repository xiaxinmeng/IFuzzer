class A:
    def close(self):
        self.close()
    def __del__(self):
        self.close()