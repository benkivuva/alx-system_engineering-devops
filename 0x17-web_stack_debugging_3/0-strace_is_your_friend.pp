# Puppet manifest to fix the bug causing Apache to return a 500 error
exec { 'sed replace .phpp file extension by .php':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
