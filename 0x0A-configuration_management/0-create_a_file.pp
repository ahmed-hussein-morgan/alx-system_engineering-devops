# a puppet to create a file 
file { '/temp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
