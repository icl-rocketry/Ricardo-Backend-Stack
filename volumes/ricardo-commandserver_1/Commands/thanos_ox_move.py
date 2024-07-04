from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

thanos_ox_move_ap = Cmd2ArgumentParser()
thanos_ox_move_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('thanos_ox_move',argparse=thanos_ox_move_ap)
def thanos_ox_move(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":102,
                        "destination_service":10,
                        "command_id":7,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)