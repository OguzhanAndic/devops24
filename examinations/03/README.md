# Examination 3 - Writing and Running an Ansible Playbook

In Examination 2 we set up our virtual machines, configured Ansible for our
purposes and made sure we were able to connect to them through SSH and use Ansible's
[ansible.builtin.ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module.

In case you added the machine you are running Ansible on in examination 2, you should remove that host now,
so your inventory only contains the Vagrant hosts, as before.

We are now ready to create and run our first Ansible playbooks.

An Ansible playbook is a file written in Ansible [YAML](https://yaml.org/) format.

Create a new file called `site.yml` with the following content:

    ---
    - name: Example Ansible playbook
      hosts: all
      tasks:
        - name: Output hostname
          ansible.builtin.debug:
            var: ansible_facts.nodename

To run this playbook, do

    $ ansible-playbook site.yml

The output should look something like this:

    PLAY [Example Ansible playbook] ******************************************************************

    TASK [Gathering Facts] ***************************************************************************
    ok: [webserver]
    ok: [dbserver]

    TASK [Output hostname] ***************************************************************************
    ok: [dbserver] => {
        "ansible_facts.nodename": "dbserver"
    }
    ok: [webserver] => {
        "ansible_facts.nodename": "webserver"
    }

    PLAY RECAP ***************************************************************************************
    dbserver   : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    webserver  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

In the output above, we can see in the `PLAY RECAP` what Ansible actually did.

* `ok` indicates that the playbook performed a task without any changes
* `changed` indicates the the playbook made a change on the machine
* `unreachable` means that Ansible could not connect to a host for some reason
* `failed` means that Ansible could connect, but failed to make a change
* `skipped` means that a conditional task was not run
* `rescued` means that a failure occurred, but but that there was a rescure procedure in place to
   continue the play
* `ignored` means that a number of hosts where ignored by this play, because they did not fulfill
   some criteria

Now, to actually make a change on the machine, we need to tell ansible to actually do something:

Make a new playbook, or edit the previous one, so that it looks like this:

    ---
    - name: Install all our favorite software
      hosts: all
      tasks:
        - name: Ensure vim, bash-completion, and qemu-guest-agent are installed
          ansible.builtin.package:
            name: vim,bash-completion,qemu-guest-agent
            state: present

You can call it whatever you like, in this example, here the name is `site.yml`.

Run this playbook, just like before:

    $ ansible-playbook site.yml

You will notice you ran into a problem:

    TASK [Ensure vim, bash-completion, and qemu-guest-agent are installed] **************************************************
    fatal: [dbserver]: FAILED! => {"changed": false, "msg": "This command has to be run under the root user.", "results": []}
    fatal: [webserver]: FAILED! => {"changed": false, "msg": "This command has to be run under the root user.", "results": []}

Obviously, it tells us we have to be `root` to install packages. Very well... we make a
small change to the task that fails in our playbook, and include a line with

    become: true

for that task. When we do this, the task itself should now look like:

    - name: Ensure vim, bash-completion, and qemu-guest-agent are installed
      become: true
      ansible.builtin.package:
        name: vim,bash-completion,qemu-guest-agent
        state: present

Run the playbook again:

    $ ansible-playbook site.yml

Now the output looks like this:

    PLAY [Install all our favorite software] **********************************************************

    TASK [Gathering Facts] ****************************************************************************
    ok: [dbserver]
    ok: [webserver]

    TASK [Ensure vim, bash-completion, and qemu-guest-agent are installed] ****************************
    changed: [dbserver]
    changed: [webserver]

    PLAY RECAP ****************************************************************************************
    dbserver    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    webserver   : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

Run the exact same playbook again and study the output. What is the difference?

## QUESTION A

What does the `ansible.builtin.debug` module actually do?

Answer: the debug module writes out the node names for every host on to the terminal when the playbook is running. this is used to be sure you are reaching out to the right hosts and to failseatch information ansible gathers from the hosts. 


## QUESTION B

What is the variable 'ansible_facts' and where does it come from?

Answer: ansible_facts is a dictonary in ansible that has information about the hosts that are managed, it contains information like ip addresses, hostnames, CPU, memory etc. Ancible_facts gathers it soource from a built in setup module as soon as you run the playbook/command. 

## QUESTION C

We now know how to use Ansible to perform changes, and to ensure these changes are still there
next time we run the playbook. This is a concept called _idempotency_.

How do we now remove the software we installed through the playbook above? Make the
playbook remove the exact same software we previously installed. Call the created
playbook `03-uninstall-software.yml`.

Answer: to remove the installed software i made a new yml file with almost an identical code, with the diffrence being that i canged the state : to absent instead of present. running the fil/playbook will change the software and give you a "changed" description on the terminal. 

## BONUS QUESTION

What happens when you run `ansible-playbook` with different options?

Explain what each of these options do:
* --verbose, -vv, -vvv, -vvvv
* --check
* --syntax-check

Answer: 
Den första * handlar om att få fram olika mycket infomration kring ansibles körningar. --v eller --verbos är den mest grundlägande extra infon, den vissar uppgifter som körs och resultat. -- vv är mer detaljerat och visar moduler som används och deras argument. -vvv är utöver det mer info, ex anslutningsinfo och ssh commands.
- vvvv är en slutlig detaljnivå på debug nivå, vilket visar allt som ex .anslutingsdetaljer, api anrop och variabelnammn.
den andra * handlar om att köra ansible playboks utan att igentligen ändra på något. Den är lite som en simulering av vad som skulle hända om du körde din ansible playbok, lite som namnet säger själv. Den "checkar" hur det skulle se ut men gör inte de riktiga ändringarna. 
den sista * är en simpel syntax chek som kollar att din playbook inte har fel synbtax. 



## Study Material & Documentation

* https://docs.ansible.com/ansible/latest/playbook_guide/playbooks.html#working-with-playbooks
* https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html
* https://docs.ansible.com/ansible/latest/collections/ansible/builtin/debug_module.html
* https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html
