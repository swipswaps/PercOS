class Command:
    name = None
    desc = None
    usage = "The usage for tis command hasn't been implemented yet"
    author = None

    @staticmethod
    def call(dire, usr, args=None):
        print("This command hasn't been implemented yet,\n if you think this is an error contact the command author")
        print("Current dir: " + dire.dir)
        if not (args is None or args == ''):
            print("Some arguments were in the call: " + args)