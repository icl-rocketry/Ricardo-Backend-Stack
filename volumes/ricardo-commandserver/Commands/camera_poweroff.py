from CommandServer.commandserver import CommandServer
import time


@CommandServer.register('camera_poweroff')
def camera_poweroff(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":14,
                        "destination_service":2,
                        "command_id":10,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)