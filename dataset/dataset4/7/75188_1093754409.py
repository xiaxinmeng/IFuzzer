import gc
import sys
import traceback

def hold_world():
    try:
        raise Exception("test1")
    except Exception as exc:
        print("exc caught in frame: ", exc.__traceback__.tb_frame)
        assert not exc.__traceback__.tb_next
        #exc.__traceback__ = None #ok
        tmp = exc
        traceback.clear_frames(exc.__traceback__) #not enough

def use_obj( o ):
    hold_world()
    #o = None #needed to get rid of the reference in the frame

def main():
    o = ["survivor"]
    print(gc.get_referrers(o))
    print(sys.getrefcount(o)) #2
    use_obj( o )
    print(gc.get_referrers(o))
    print(sys.getrefcount(o)) #3
    #o = None #needed to get rid of the reference in the frame

if __name__ == '__main__':
    main()