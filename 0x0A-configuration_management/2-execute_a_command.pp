# a puppet manifest that kills a process named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
