from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pickle_enter_preflight_ap = Cmd2ArgumentParser()
pickle_enter_preflight_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('pickle_enter_preflight',argparse=pickle_enter_preflight_ap)
def pickle_enter_preflight(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":101,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)