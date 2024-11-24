from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pdu_restartlogic_ap = Cmd2ArgumentParser()
pdu_restartlogic_ap.add_argument("--destination",type=int,required=True)
pdu_restartlogic_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('pdu_restartlogic',argparse=pdu_restartlogic_ap)
def pdu_restartlogic(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":2,
                        "command_id":3,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)