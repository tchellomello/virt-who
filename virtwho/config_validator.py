# -*- coding: utf-8 -*-
import voluptuous as vol

VW_TYPES = ("libvirt", "vdsm", "esx", "rhevm", 
            "hyperv", "fake", "xen", "kubevirt")

def string(value):
    if value is not None:
        return str(value)
    raise vol.Invalid("value is not a string or empty")

def hypervisor(value):
    """Validate if hypervisor is supportability."""
    if value not in VW_TYPES:
        raise vol.Invalid("type '%s' is not valid" % value)
    return value

# Define voluptuous schema for dropdir files
VW_SCHEMA = vol.Schema({
    vol.Required('type'): hypervisor,
    vol.Required('server'): string,
    vol.Required('username'): string,
    vol.Required('password'): string,
    vol.Required('encrypted_password'): string,
    vol.Required('owner'): string,
    vol.Required('env'): string,
    vol.Required('hypervisor_id'): string,

    vol.Optional('rhsm_hostname'): string,
    vol.Optional('rhsm_port'): string,
    vol.Optional('rhsm_prefix'): string,
    vol.Optional('rhsm_username'): string,
    vol.Optional('rhsm_password'): string,
    vol.Optional('rhsm_encrypted_password'): string,
    vol.Optional('rhsm_proxy_hostname'): string,
    vol.Optional('rhsm_proxy_port'): string,
    vol.Optional('rhsm_proxy_user'): string,
    vol.Optional('rhsm_proxy_password'): string,
    vol.Optional('rhsm_insecure'): string,
})
