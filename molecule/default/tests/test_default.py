import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cron_generated(host):
    cmd = host.run('crontab -l')
    assert cmd.rc == 0
    assert cmd.stdout.strip() == (
        '#Ansible: example\n'
        r'0 1 2 3 4 /bin/echo \%100\%'
    )
