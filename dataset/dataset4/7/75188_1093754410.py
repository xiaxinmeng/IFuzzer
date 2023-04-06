import gc
import refcycle
import sys
import traceback

def hold_world():
    try:
        raise Exception("test1")
    except Exception as exc:
        tmp = exc

def use_obj( o ):
    hold_world()

def main():
    gc.disable()
    gc.collect()
    o = ["survivor"]
    use_obj( o )
    garbage = refcycle.garbage()
    garbage.export_image()


if __name__ == '__main__':
    main()