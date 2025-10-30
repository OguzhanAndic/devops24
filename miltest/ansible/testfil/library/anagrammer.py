#!/usr/bin/env python3
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        message=dict(type='str', required=True)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )
    message = module.params['message']
    reversed_message = message[::-1]

    # sätt värdena i resultatet
    changed = message != reversed_message

    # om användaren skriver "fail me"
    if message == "fail me":
        module.fail_json(
            msg="You requested this to fail",
            changed=True,
            original_message=message,
            reversed_message=reversed_message
        )

    # changed ska vara True om meddelandet skiljer sig från den omvända versionen


    module.exit_json(                     
        changed=changed,
        original_message=message,
        reversed_message=reversed_message
    )

def main():
    run_module()

if __name__ == '__main__':
    main()
