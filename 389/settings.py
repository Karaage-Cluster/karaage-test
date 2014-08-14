LDAP = {
    'default': {
        'ENGINE': 'tldap.backend.fake_transactions',
        'URI': 'ldap://localhost',
        'USER': 'cn=Directory Manager',
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
            'ACCOUNT': 'karaage.datastores.ldap_schemas.ds389_account',
            'GROUP': 'karaage.datastores.ldap_schemas.ds389_account_group',
            'PRIMARY_GROUP': "institute",
            'DEFAULT_PRIMARY_GROUP': "dummy",
            'HOME_DIRECTORY': "/home/%(uid)s",
            'LOCKED_SHELL': "/usr/local/sbin/locked",
            'LDAP_ACCOUNT_BASE': _ldap_person_base,
            'LDAP_GROUP_BASE': _ldap_group_base,
        },
    ],
    'dummy': [
    ],
}

LDAP_PEOPLE = False
if LDAP_PEOPLE and _ldap_account_base:
    GLOBAL_DATASTORES = [
        {
            'DESCRIPTION': 'LDAP datastore',
            'ENGINE': 'karaage.datastores.ldap.GlobalDataStore',
            'LDAP': 'default',
            'PERSON': 'karaage.datastores.ldap_schemas.ds389_person',
            'GROUP': 'karaage.datastores.ldap_schemas.ds389_person_group',
            'LDAP_PERSON_BASE': _ldap_person_base,
            'LDAP_GROUP_BASE': _ldap_group_base,
        },
    ]
    MACHINE_CATEGORY_DATASTORES['ldap'][0]['LDAP_ACCOUNT_BASE'] = \
        _ldap_account_base
