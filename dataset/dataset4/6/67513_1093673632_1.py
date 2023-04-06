def run(self):
        """
        This method continually runs. If an incoming character is available on the serial port
        it is read and placed on the _command_deque
        @return: Never Returns
        """
        while not self.is_stopped():
            # we can get an OSError: [Errno9] Bad file descriptor when shutting down
            # just ignore it
            try:
                if self.arduino.inWaiting():
                    c = self.arduino.read()
                    self.command_deque.append(ord(c))
            except OSError:
                pass
            except IOError:
                self.stop()
        self.close()