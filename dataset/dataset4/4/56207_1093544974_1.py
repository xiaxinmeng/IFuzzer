allsignals = range(1, signal.NSIG)
oldmask = signal.pthread_sigmask(signal.SIG_BLOCK, allsignals)
import _tkinter
signal.pthread_sigmask(signal.SIG_SETMASK, oldmask)