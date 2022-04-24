import os
import socket
from pulumi import automation
from fanqiangpulumi import proxy


def test_service_port():
    project_name = automation.LocalWorkspace(os.getcwd()).project_settings().name
    stack = automation.create_or_select_stack(__name__, project_name, proxy.apply)
    try:
        result = stack.up(on_output=print)
        with socket.create_connection(
            (result.outputs["host"].value, result.outputs["port"].value)
        ):
            pass
    finally:
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack.name)
