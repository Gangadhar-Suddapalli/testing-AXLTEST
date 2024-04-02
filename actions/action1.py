from st2common.runners.base_action import Action
class ConcatenateStringsAction(Action):
    def run(self, string1, string2):
        concatenated_string = string1 + string2
        return {"concatenated_string": concatenated_string}

