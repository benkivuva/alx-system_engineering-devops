# 7-puppet_install_nginx_web_server.pp
# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        echo \"Hello World!\";
    }

    location /redirect_me {
        rewrite ^ http://www.github.com permanent;
    }
}
",
  require => Package['nginx'],
}

# Enable the default site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
  subscribe => [File['/etc/nginx/sites-available/default'], File['/etc/nginx/sites-enabled/default']],
}
