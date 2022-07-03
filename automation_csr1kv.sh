#!/bin/bash

ansible-playbook csr1kv_config.yaml
ansible-playbook backup_csr1kv_config.yaml

