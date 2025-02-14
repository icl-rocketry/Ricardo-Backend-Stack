from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

setthanosoxlag_ap = Cmd2ArgumentParser()
setthanosoxlag_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('setthanosoxlag',argparse=setthanosoxlag_ap)
def setthanosoxlag(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":2,
                        "destination_service":10,
                        "command_id":8,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)

