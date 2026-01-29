# Ansible Lab: Infrastructure Automation Basics

## Overview

This project is a practical laboratory work focused on learning Ansible fundamentals.
It demonstrates how to automate basic infrastructure tasks on Linux hosts using Ansible playbooks.

The lab was built and tested on Ubuntu virtual machines and covers host connectivity checks,
service installation, configuration management, and basic network diagnostics.

---

## Environment

- Ansible Controller: Linux (WSL)
- Managed nodes: 2 × Ubuntu Server virtual machines
- Virtualization: VMware (NAT networking)
- Configuration management tool: Ansible

---

## Project Structure

ansible-lab/
├── ansible.cfg # Ansible configuration file
├── inventory/
│ └── hosts.txt # Inventory with managed hosts
├── group_vars/
│ └── lab.yml # Group variables
├── files/
│ └── index.html # Static web page for Apache
├── playbooks/
│ ├── check_hosts.yml # Connectivity and fact gathering
│ ├── apache.yml # Apache installation and configuration
│ └── network_diagnostics.yml # Network diagnostics playbook
└── README.md

## Implemented Playbooks

### 1. Host Connectivity Check

check_hosts.yml verifies that managed hosts are reachable and gathers system facts.

Used modules:
- ping
- setup

---

### 2. Apache Installation and Configuration

apache.yml performs the following tasks:
- Installs Apache HTTP Server
- Ensures the service is running and enabled at boot
- Deploys a static index.html page to /var/www/html/

This playbook demonstrates basic package management, service control, and file deployment.

---

### 3. Network Diagnostics

network_diagnostics.yml collects basic network information from managed hosts, including:
- IP addressing
- Routing table
- Active network interfaces

This playbook is useful for initial infrastructure troubleshooting and verification.

---

## How to Run

From the project root directory:

ansible-playbook playbooks/check_hosts.yml
ansible-playbook playbooks/apache.yml
ansible-playbook playbooks/network_diagnostics.yml

## Result

After running the Apache playbook, the web server becomes accessible on each managed node
via its IP address on port 80, serving the deployed static page.

## Purpose

This project was created as part of hands-on learning of Ansible and infrastructure automation.
It serves as a foundation for more advanced topics such as roles, templates, handlers, and CI/CD integration.
