Ansible role: cron
==================

[![Build Status](https://travis-ci.org/apkawa/ansible-role-cron.svg?branch=master)](https://travis-ci.org/apkawa/ansible-role-cron)

[![Ansible role](https://img.shields.io/ansible/role/42590.svg)](https://galaxy.ansible.com/apkawa/cron)
[![Ansible role downloads](https://img.shields.io/ansible/role/d/42590.svg)](https://galaxy.ansible.com/apkawa/cron)
[![Ansible role quality](https://img.shields.io/ansible/quality/42590.svg)](https://galaxy.ansible.com/apkawa/cron)

A brief description of the role goes here.

Requirements
------------

None

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):
```yaml
cron:
  # required
  -  
      name: cron_name
      command: /bin/true
      # defaults
      user: "{{ ansible_ssh_user }}"
      minute: "*"
      hour: "*"
      day: "*"
      month: "*"
      weekday: "*"

      delete: false
   - 
      name: cron_for_delete
      delete: true 
```

https://crontab.guru/

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-cron

```

License
-------

MIT 

Author Information
------------------

Apkawa 

