#2. Execute a command
exec { 'pkill killmenow':
  provider => 'shell'
}
