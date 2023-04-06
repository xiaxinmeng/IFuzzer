import  sys
import  multiprocessing
import  multiprocessing.forking


#
#
#
#
def duplicate(handle, target_process = None, inheritable = True) :
    return(multiprocessing.forking.kludge_to_fix_dangling_processes(handle, target_process, inheritable))