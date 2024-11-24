from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

import time

blackbox_updateTime = Cmd2ArgumentParser()


@CommandServer.register("blackbox_updateTime", argparse=blackbox_updateTime)
def blackbox_updateTime(instance, args):

    command_packet_args = {
        "source": 1,
        "source_service": instance.source_service,
        "destination": 20,
        "destination_service": 123,
        "command_id": 0,
        "command_arg": int(time.time()),
    }

    instance.send_command_packet(command_packet_args)
