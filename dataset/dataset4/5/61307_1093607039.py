import queue
import socket

class Demo(object):
  def __init__(self, control_socket_file):
    demo_queue = queue.Queue()