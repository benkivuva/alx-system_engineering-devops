# puppet manifest to fix issue
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
