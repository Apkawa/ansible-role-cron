Role Name
=========

[![Build Status](https://travis-ci.org/apkawa/ansible-role-cron.svg?branch=master)](https://travis-ci.org/apkawa/ansible-role-cron)

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

