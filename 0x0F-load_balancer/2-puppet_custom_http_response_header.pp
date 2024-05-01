# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d':
  ensure  => directory,
  mode    => '0755',
  owner   => 'root',
  group   => 'root',
}

# Configure Nginx to include the custom HTTP header
file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure  => file,
  content => "server {
    listen 80;
    server_name _;
    location / {
      add_header X-Served-By ${::hostname};
    }
  }",
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

