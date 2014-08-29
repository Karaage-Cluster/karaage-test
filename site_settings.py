_ldap_base = 'dc=example,dc=org'
_ldap_old_account_base = 'ou=People,%s' % _ldap_base
_ldap_old_group_base = 'ou=Groups,%s' % _ldap_base
_ldap_person_base = 'ou=People,%s' % _ldap_base
_ldap_person_group_base = 'ou=People_Groups,%s' % _ldap_base
_ldap_account_base = 'ou=Accounts,%s' % _ldap_base
_ldap_account_group_base = 'ou=Groups,%s' % _ldap_base
_ldap_user = 'cn=admin,%s' % _ldap_base
_ldap_password = 'slapdsecret'
