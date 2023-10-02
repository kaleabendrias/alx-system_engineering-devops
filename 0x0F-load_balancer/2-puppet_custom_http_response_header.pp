# Use Puppet to automate the task of creating a custom HTTP header response

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure => 'installed',
}

file_line { 'add_header':
  path   => '/etc/nginx/sites-enabled/default',
  after  => "^\tlocation / {",
  line   => "\t\tadd_header X-Served-By \"${::hostname}\";",
  notify => Exec['run'],
}

exec {'run':
  command => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
