# Install Nginx
package { 'nginx':
 ensure => installed,
}

# Ensure Nginx is running and enabled to start at boot
service { 'nginx':
 ensure     => running,
 enable     => true,
 require    => Package['nginx'],
}

# Ensure Nginx is listening on port 80
firewall { '80':
 port   => '80',
 proto => 'tcp',
 action => 'accept',
}

# Configure Nginx to serve a page containing "Hello World!" at its root
file { '/var/www/html/index.nginx-debian.html':
 ensure => file,
 content => '<html><body><h1>Hello World!</h1></body></html>',
 require => Package['nginx'],
}

# Set up a 301 redirect from /redirect_me to another URL
file { '/etc/nginx/sites-available/default':
 ensure => file,
 content => template('nginx/default.erb'),
 require => Package['nginx'],
 notify => Service['nginx'],
}

# Ensure the default site is enabled
file { '/etc/nginx/sites-enabled/default':
 ensure => link,
 target => '/etc/nginx/sites-available/default',
 require => File['/etc/nginx/sites-available/default'],
 notify => Service['nginx'],
}

