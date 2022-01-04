#Client configuration file (w/ Puppet)

file_line {'identity':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line {'password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  replace => true,
}
