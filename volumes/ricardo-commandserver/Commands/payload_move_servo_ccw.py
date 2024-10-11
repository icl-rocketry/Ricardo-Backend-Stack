from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

payload_move_servo_ccw_ap = Cmd2ArgumentParser()
payload_move_servo_ccw_ap.add_argument("--destination_service",type=int,required=True)
payload_move_servo_ccw_ap.add_argument('--duration',type=float,required=False,default=1)

@CommandServer.register('payload_move_payload_move_servo_ccw',argparse=payload_move_servo_ccw_ap)
def payload_move_servo_ccw(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":200,
                        "destination_service":20,
                        "command_id":2,
                        "command_arg":110}

    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(args.get('duration',1))
    command_packet_args['command_arg'] = 90
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)
    time.sleep(0.02)
    instance.send_command_packet(command_packet_args)

    return True