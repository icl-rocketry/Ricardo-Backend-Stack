from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pickle_reset_orientation_ap = Cmd2ArgumentParser()
pickle_reset_orientation_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('pickle_reset_orientation',argparse=pickle_reset_orientation_ap)
def pickle_reset_orientation(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":50,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)