sendmsg = getattr(socket.socket, "sendmsg", False)

# [snip]
def writelines(self, lines):
    if not sendmsg:
        return self.write(b''.join(lines))
    # [snip]