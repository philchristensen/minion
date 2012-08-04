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
	path		= ,
	hasstatus	= True,
	path => "/etc/postgresql/8.4/main/pg_hba.conf",
	content => template("fu-web/pg_hba.conf.production.erb"),
	require => Package['postgresql84'],
	notify => Service['postgresql'],
)