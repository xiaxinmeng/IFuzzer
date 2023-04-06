import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
aboutdialog = Gtk.AboutDialog()
aboutdialog.set_name('arbitrary')
aboutdialog.run()
aboutdialog.destroy()