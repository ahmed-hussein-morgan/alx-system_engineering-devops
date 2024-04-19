# kill a process named killmenow

exec { 'pkill killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  onlyif  => 'pgrep killmenow',
}
