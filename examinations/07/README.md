# Examination 7 - MariaDB installation

To make a dynamic web site, many use an SQL server to store the data for the web site.

[MariaDB](https://mariadb.org/) is an open-source relational SQL database that is good
to use for our purposes.

We can use a similar strategy as with the _nginx_ web server to install this
software onto the correct host(s). Create the playbook `07-mariadb.yml` with this content:

    ---
    - hosts: db
      become: true
      tasks:
        - name: Ensure MariaDB-server is installed.
          ansible.builtin.package:
            name: mariadb-server
            state: present

# QUESTION A

Make similar changes to this playbook that we did for the _nginx_ server, so that
the `mariadb` service starts automatically at boot, and is started when the playbook
is run.

Answer: the playbook has been made and modified. 

# QUESTION B

When you have run the playbook above successfully, how can you verify that the `mariadb`
service is started and is running?

Answer: ny using ssh to go in to the vm and then using the command: sudo systemctl status mariadb. this will show you some information about the mariadb.service. If the "Active" field says active (running), the service is running. 

# BONUS QUESTION

How many different ways can use come up with to verify that the `mariadb` service is running?

Answer: sudo systemctl status mariadb is probably one of the easiest ways to check, but you could also make a when: in the playbook to make sure that every thing works when you put up the vm with the ansible playbook. 