import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_is_installed(Package):
    nginx = Package("nginx")
    assert nginx.is_installed


def test_command_output(Command):
    command = Command('nginx -t')
    assert command.rc == 0


def test_service_running(Service):
    service = Service('nginx')
    assert service.is_running
    assert service.is_enabled
