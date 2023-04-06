import codecs

import pygtk
import gtk

f = codecs.open( "test.iso-2022-jp-2" , "r" , \
                 "iso-2022-jp-2" )
s1 = f.readline().strip()
f.close()

f = open( "test.utf-8" , "r" )
s2 = f.readline().strip()

pack = gtk.VBox()
pack.pack_start( gtk.Label( s1 ) )
pack.pack_start( gtk.Label( s2 ) )

window = gtk.Window( gtk.WINDOW_TOPLEVEL )
window.add( pack )
window.show_all()

def event_destroy( widget , event , data ) :
    gtk.main_quit()
    return 0

window.connect( "delete_event" , \
                lambda w,e,d: False , None )
window.connect( "destroy" , event_destroy , None )

gtk.main()