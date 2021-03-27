# using puppet to automate the process of managing multiple machines in a fleet

class packages {
# ensure the python-requests package is installed on all machines in the fleet
   package { 'python-requests':
       ensure => installed,
   }

   # ensure the golang package is installed on machines with Debian OS
   if $facts[os][family] == "Debian" {
     package { 'golang':
       ensure => installed,
     }
  }

  # ensure the nodejs package is installed on machines with RedHat OS
   if $facts[os][family] == "RedHat" {
     package { 'nodejs':
       ensure => installed,
     }
  }
}