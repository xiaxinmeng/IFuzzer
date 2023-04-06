class MyCmd(cmd.Cmd):

    parser = argparse.ArgumentParser(prog='addobject')
    parser.add_argument('attribute1')
    parser.add_argument('attribute2')
    parser.add_argument('attribute3')

    def do_addobject(self, line):
        args = MyCmd.parser.parse_args(line.split())
        newobject = object(args.attribute1, args.attribute2, args.attribute3)
        myobjects.append(newobject)