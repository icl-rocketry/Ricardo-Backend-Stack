from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

oxvent_srv_move_ap = Cmd2ArgumentParser()
oxvent_srv_move_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('oxvent_srv_move',argparse=oxvent_srv_move_ap)
def oxvent_srv_move(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":103,
                        "destination_service":11,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)

