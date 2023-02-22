from Controller.Controller import Controller
from Arg_Parser.arg_parser import Arg_Parser

if __name__ == "__main__":
    test = Arg_Parser()
    launch = Controller()
    launch.decide_where_to_start()




