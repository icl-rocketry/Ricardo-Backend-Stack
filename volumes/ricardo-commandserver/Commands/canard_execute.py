from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

canard_execute_ap = Cmd2ArgumentParser()
canard_execute_ap.add_argument("--destination",type=int,required=True)
canard_execute_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('canard_execute',argparse=canard_execute_ap)
def canard_execute(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)

