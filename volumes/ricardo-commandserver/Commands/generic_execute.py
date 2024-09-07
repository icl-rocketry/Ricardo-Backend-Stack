from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

generic_execute_ap = Cmd2ArgumentParser()
generic_execute_ap.add_argument("--destination",type=int,required=True)
generic_execute_ap.add_argument("--destination_service",type=int,required=True)
generic_execute_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('generic_execute',argparse=generic_execute_ap)
def generic_execute(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)
