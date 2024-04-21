# config server using puppet
# set up the client SSH configuration file using puppet

file { '/etc/ssh/ssh_config':
  ensure => 'present',
  owner   => 'ubuntu',
  content => "Host *\n IdentityFile ~/.ssh/school\n PasswordAuthentication no\n",
}
