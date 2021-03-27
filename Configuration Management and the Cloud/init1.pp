''' If this file was in a real puppet environment it would be named init.pp but i had to add 1 at the end so i can have both of my init.pp files in the same directory. '''


''' In this puppet code we will be creating a new module named reboot, that checks
if a node has been online for more than 30 days. If so, then reboot the computer. '''


class reboot {
  if $facts[kernel] == "windows" {
    $cmd = "shutdown /r"
  } elsif $facts[kernel] == "Darwin" {
    $cmd = "shutdown -r now"
  } else {
    $cmd = "reboot"
  }
  
  if $facts[uptime_days] > 30 {
    exec { 'reboot':
      command => $cmd,
     }
   }
}