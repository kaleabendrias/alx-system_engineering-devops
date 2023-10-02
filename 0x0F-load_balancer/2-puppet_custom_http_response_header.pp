# Use Puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure => 'installed',
}

-> file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "	location / {
  add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

exec {'run':
  command => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
