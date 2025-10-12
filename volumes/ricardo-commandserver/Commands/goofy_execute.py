from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

goofy_execute_ap = Cmd2ArgumentParser()
goofy_execute_ap.add_argument("--argument",type=int,required=True)

@CommandServer.register('goofy_execute',argparse=goofy_execute_ap)
def goofy_execute(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":8,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)

