LDAP = {
    'default': {
        'ENGINE': 'tldap.backend.fake_transactions',
        'URI': 'ldap://localhost',
        'USER': _ldap_user,
        'PASSWORD': _ldap_password,
        'REQUIRE_TLS': False,
        'START_TLS': False,
        'TLS_CA': None,
    }
}

MACHINE_CATEGORY_DATASTORES = {
    'ldap': [
        {
            'DESCRIPTION': 'LDAP datastore',
            'ENGINE': 'karaage.datastores.ldap.MachineCategoryDataStore',
            'LDAP': 'default',
            'ACCOUNT': 'karaage.datastores.ldap_schemas.openldap_account',
            'GROUP': 'karaage.datastores.ldap_schemas.openldap_account_group',
            'PRIMARY_GROUP': "institute",
            'DEFAULT_PRIMARY_GROUP': "dummy",
            'HOME_DIRECTORY': "/home/%(uid)s",
            'LOCKED_SHELL': "/usr/local/sbin/locked",
            'LDAP_ACCOUNT_BASE': _ldap_old_account_base,
            'LDAP_GROUP_BASE': _ldap_old_group_base,
            'OLD_ACCOUNT_BASE': _ldap_old_account_base,
            'OLD_GROUP_BASE': _ldap_old_group_base,
        },
    ],
    'dummy': [
    ],
}

LDAP_PEOPLE = False
if LDAP_PEOPLE and _ldap_person_base:
    GLOBAL_DATASTORES = [
        {
            'DESCRIPTION': 'LDAP datastore',
            'ENGINE': 'karaage.datastores.ldap.GlobalDataStore',
            'LDAP': 'default',
            'PERSON': 'karaage.datastores.ldap_schemas.openldap_person',
            'GROUP': 'karaage.datastores.ldap_schemas.openldap_person_group',
            'LDAP_PERSON_BASE': _ldap_person_base,
            'LDAP_GROUP_BASE': _ldap_person_group_base,
        },
    ]
if LDAP_PEOPLE:
    MACHINE_CATEGORY_DATASTORES['ldap'][0]['LDAP_ACCOUNT_BASE'] = \
        _ldap_account_base
    MACHINE_CATEGORY_DATASTORES['ldap'][0]['LDAP_GROUP_BASE'] = \
        _ldap_account_group_base
