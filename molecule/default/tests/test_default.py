import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    cmd = host.run('crontab -l')
    assert cmd.rc == 0
    assert cmd.stdout.strip() == (
        '#Ansible: example\n'
        '0 1 2 3 4 /bin/true'
    )
