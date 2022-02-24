#task-0
exec { 'fix-nginx':
  command  => 'sed -i s/15/4069/ /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
