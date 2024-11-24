from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pickle_set_home_ap = Cmd2ArgumentParser()
pickle_set_home_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('pickle_set_home',argparse=pickle_set_home_ap)
def pickle_set_home(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)