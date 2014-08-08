LDAP = {
    'default': {
        'ENGINE': 'tldap.backend.fake_transactions',
        'URI': 'ldap://localhost',
        'USER': 'cn=admin,dc=example,dc=org',
        'PASSWORD': 'slapdsecret',
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
            'LDAP_ACCOUNT_BASE': 'ou=People,dc=example, dc=org',
            'LDAP_GROUP_BASE': 'ou=Groups,dc=example, dc=org',
        },
    ],
    'dummy': [
    ],
}

LDAP_PEOPLE = False
if LDAP_PEOPLE:
    GLOBAL_DATASTORES = [
        {
            'DESCRIPTION': 'LDAP datastore',
            'ENGINE': 'karaage.datastores.ldap.GlobalDataStore',
            'LDAP': 'default',
            'PERSON': 'karaage.datastores.ldap_schemas.openldap_person',
            'GROUP': 'karaage.datastores.ldap_schemas.openldap_person_group',
            'LDAP_PERSON_BASE': 'ou=People,dc=example, dc=org',
            'LDAP_GROUP_BASE': 'ou=Groups,dc=example, dc=org',
        },
    ]
    MACHINE_CATEGORY_DATASTORES['ldap'][0]['LDAP_ACCOUNT_BASE'] = \
        'ou=Accounts,dc=example, dc=org'
