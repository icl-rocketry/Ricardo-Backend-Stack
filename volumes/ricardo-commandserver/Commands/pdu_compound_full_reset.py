from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

pdu_compound_full_reset_ap = Cmd2ArgumentParser()
pdu_compound_full_reset_ap.add_argument("--destination0",type=int,required=True)
pdu_compound_full_reset_ap.add_argument("--destination1",type=int,required=True)
pdu_compound_full_reset_ap.add_argument("--restart_duration",type=int,required=True)
@CommandServer.register('pdu_compound_full_reset',argparse=pdu_compound_full_reset_ap)
def pdu_compound_full_reset(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination0'],
                        "destination_service":2,
                        "command_id":1,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

    time.sleep(0.001)
    command_packet_args['destination'] = args['destination1']

    instance.send_command_packet(command_packet_args)
    
    time.sleep(0.001)
    
    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination0'],
                        "destination_service":2,
                        "command_id":3,
                        "command_arg":args['restart_duration']}
    
    instance.send_command_packet(command_packet_args)

    time.sleep(0.001)
    command_packet_args['destination'] = args['destination1']

    instance.send_command_packet(command_packet_args)