from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

valve_sol_close_ap = Cmd2ArgumentParser()
valve_sol_close_ap.add_argument("--destination",type=int,required=True)
valve_sol_close_ap.add_argument("--destination_service",type=int,required=True)

@CommandServer.register('valve_sol_close',argparse=valve_sol_close_ap)
def valve_sol_close(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

