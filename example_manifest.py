from minion import *

Package('postgresql91',
	name		= 'postgresql91-server',
	ensure		= present,
	provider	= apt,
	configfiles	= keep,
)

Service('postgresql',
	ensure		= running,
	enable		= True,
	hasrestart	= True,
	hasstatus	= True,
)

File('postgres-hba',
	ensure		= present,
	backup		= False,
	path = "/etc/postgresql/9.1/main/pg_hba.conf",
	content = template("fu-web/pg_hba.conf.production.erb"),
	require = Package['postgresql91'],
	notify = Service['postgresql'],
)

Exec('postgresql-setup-user',
	command = '/usr/bin/psql -U postgres -c "CREATE USER minion WITH PASSWORD \'minion\';"',
	returns = [0,1],
	require = [File['postgres-hba']],
)

Exec('postgresql-setup-db',
	command = '/usr/bin/psql -U postgres -c "CREATE DATABASE minion WITH OWNER minion;"',
	returns = [0,1],
	require = [Exec['postgresql-setup-user']],
)

