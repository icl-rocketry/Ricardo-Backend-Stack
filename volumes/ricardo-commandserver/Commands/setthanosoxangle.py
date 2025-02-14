from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

setthanosoxangle_ap = Cmd2ArgumentParser()
setthanosoxangle_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('setthanosoxangle',argparse=setthanosoxangle_ap)
def setthanosoxangle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":2,
                        "destination_service":10,
                        "command_id":6,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)