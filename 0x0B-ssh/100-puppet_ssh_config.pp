# client configuration using puppet
exec { '/etc/ssh/ssh_config':
  path    => '/usr/bin/',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}
