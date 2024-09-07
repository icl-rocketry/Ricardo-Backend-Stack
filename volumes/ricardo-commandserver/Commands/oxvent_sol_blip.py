from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

oxvent_sol_blip_ap = Cmd2ArgumentParser()
oxvent_sol_blip_ap.add_argument("--destination",type=int,required=True)
oxvent_sol_blip_ap.add_argument("--destination_service",type=int,required=True)
oxvent_sol_blip_ap.add_argument('--duration',type=float,required=False,default=1)

@CommandServer.register('oxvent_sol_blip',argparse=oxvent_sol_blip_ap)
def oxvent_sol_blip(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":2,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)
    time.sleep(args.get('duration',1))
    command_packet_args['command_arg'] = 0
    instance.send_command_packet(command_packet_args)
    return True