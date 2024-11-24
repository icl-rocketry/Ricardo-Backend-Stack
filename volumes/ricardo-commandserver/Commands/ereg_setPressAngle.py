from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

ereg_setPressAngle_ap = Cmd2ArgumentParser()
ereg_setPressAngle_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('ereg_setPressAngle',argparse=ereg_setPressAngle_ap)
def ereg_setPressAngle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":13,
                        "destination_service":10,
                        "command_id":7,
                        "command_arg":10*args['argument']}

    instance.send_command_packet(command_packet_args)
