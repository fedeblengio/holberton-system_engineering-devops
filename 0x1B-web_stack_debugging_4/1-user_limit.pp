#task-1
exec { 'fix-soft':
  provider => 'shell',
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 55000/g" /etc/security/limits.conf'
}

exec { 'fix-hard':
  provider => 'shell',
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 55000/g" /etc/security/limits.conf'
}
