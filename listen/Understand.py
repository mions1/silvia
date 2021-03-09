from commands import builtin

class Understand:

    def __init__(self):
        pass

    def command_from_speech(self, text):
        comm_builtin = builtin.Builtin(text)
        result = comm_builtin.recognize_and_execute()
        if not result and result != "":
            return comm_builtin.unknown()
        return result
