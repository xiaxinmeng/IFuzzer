### start of example ###
import curses                                                                                                                               
                                                                                                                                            
                                                                                                                                            
def main(stdscr):                                                                                                                           
    curses.start_color()                                                                                                                    
    curses.use_default_colors()                                                                                                             
    curses.init_pair(1, curses.COLOR_RED, -1)                                                                                               
    curses.init_pair(2, curses.COLOR_GREEN, -1)                                                                                             
    curses.curs_set(0)                                                                                                                      
                                                                                                                                            
    stdscr.addch("a", curses.color_pair(1))                                                                                                 
    stdscr.addch("b", curses.color_pair(2) | curses.A_BOLD)                                                                                 
    stdscr.addch(b"c", curses.color_pair(1))                                                                                                
    stdscr.addch(b"d", curses.color_pair(2) | curses.A_BOLD)                                                                                
    stdscr.addch(ord("e"), curses.color_pair(1))                                                                                            
    stdscr.addch(ord("f"), curses.color_pair(2) | curses.A_BOLD)                                                                            
    stdscr.refresh()                                                                                                                        
                                                                                                                                            
    stdscr.getch()                                                                                                                          
                                                                                                                                            
                                                                                                                                            
curses.wrapper(main)                                                                                                                        
### end of example ###