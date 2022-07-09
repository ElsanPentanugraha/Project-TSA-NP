#!/bin/bash

python3 ipaddconfig2.py
ansible-playbook csr1kv_config.yaml
ansible-playbook backup_csr1kv_config.yaml

