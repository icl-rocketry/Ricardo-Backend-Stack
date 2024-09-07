from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

ereg_setPessAngle_ap = Cmd2ArgumentParser()
ereg_setPessAngle_ap.add_argument("--destination",type=int,required=True)
ereg_setPessAngle_ap.add_argument("--destination_service",type=int,required=True)
ereg_setPessAngle_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('ereg_setPessAngle',argparse=ereg_setPessAngle_ap)
def ereg_setPessAngle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":7,
                        "command_arg":10*args['argument']}

    instance.send_command_packet(command_packet_args)
