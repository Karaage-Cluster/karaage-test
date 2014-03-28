# Globally defined Karaage settings
# These settings will be used for karaage-admin and/or karaage-registration
###
### Standard Django settings 
### see http://docs.djangoproject.com/en/1.2/ref/settings/#ref-settings
###

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SESSION_COOKIE_SECURE = False

# Will receive error reports if something goes wrong
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'karaage',                    # Or path to database file if using sqlite3.
        'USER': 'karaage',                    # Not used with sqlite3
        'PASSWORD': 'mysqlsecret',            # Not used with sqlite3.
        'HOST': '',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
        'ATOMIC_REQUESTS': True,
    }
}

# Defaults used for error reports
SERVER_EMAIL = 'karaage@example.org'
EMAIL_HOST = 'localhost'
EMAIL_SUBJECT_PREFIX = '[Karaage] - '

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Australia/Melbourne'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-au'

# Unique key used for storing session data etc.
SECRET_KEY = ''

###
### Karaage settings
###

# Do new cluster accounts need a 2nd stage of approval
ADMIN_APPROVE_ACCOUNTS = True

# Used in various places
ACCOUNTS_EMAIL = 'accounts@example.com'
ACCOUNTS_ORG_NAME = 'Example'
# Address email is sent to for admin approval
APPROVE_ACCOUNTS_EMAIL = ACCOUNTS_EMAIL

LOCKED_SHELL = '/usr/local/sbin/insecure'

# Registration base URL - Used in email templates
# Uncomment to override default
# REGISTRATION_BASE_URL = 'https://<hostname>/users'


###
### Placard Settings
### see - https://code.vpac.org/hudson/job/django-placard/javadoc/
###


LDAP = {
    'default': {
        'ENGINE': 'tldap.backend.fake_transactions',
        'URI': 'ldap://localhost',
        'USER': 'cn=Directory Manager',
        'PASSWORD': 'slapdsecret',
        'REQUIRE_TLS': False,
        'START_TLS': False,
        'TLS_CA' : None,
    }
}

MACHINE_CATEGORY_DATASTORES = {
    'ldap' : [
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
            'LDAP_ACCOUNT_BASE': 'ou=People,dc=example, dc=org',
            'LDAP_GROUP_BASE': 'ou=Groups,dc=example, dc=org',
        },
    ],
    'dummy' : [
    ],
}

LDAP_PEOPLE = False
if LDAP_PEOPLE:
    GLOBAL_DATASTORES = [
        {
            'DESCRIPTION': 'LDAP datastore',
            'ENGINE': 'karaage.datastores.ldap.GlobalDataStore',
            'LDAP': 'default',
            'PERSON': 'karaage.datastores.ldap_schemas.ds389_person',
            'GROUP': 'karaage.datastores.ldap_schemas.ds389_person_group',
            'LDAP_PERSON_BASE': 'ou=People,dc=example, dc=org',
            'LDAP_GROUP_BASE': 'ou=Groups,dc=example, dc=org',
        },
    ]
    MACHINE_CATEGORY_DATASTORES['ldap'][0]['LDAP_ACCOUNT_BASE'] = 'ou=Accounts,dc=example, dc=org'


###
### Django PBS settings
###


LOCAL_PBS_SERVERS = [
]

ALLOWED_HOSTS = ['localhost']
