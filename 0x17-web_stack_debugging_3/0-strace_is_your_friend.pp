# apt-get install -y ruby
# gem install puppet-lint -v 2.1.1


exec{ 'strace-is-your-friend':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
