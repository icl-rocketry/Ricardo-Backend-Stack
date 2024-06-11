from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

fuelventsol_pyr_fire_ap = Cmd2ArgumentParser()
fuelventsol_pyr_fire_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('fuelventsol_pyr_fire',argparse=fuelventsol_pyr_fire_ap)
def fuelventsol_pyr_fire(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
                        "destination_service":11,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)