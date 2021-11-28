# URI addresses
KITC app
https://tazik1.swedencentral.cloudapp.azure.com/
Moodle
https://tazik1.swedencentral.cloudapp.azure.com/moodle/
MySQL 8.0
https://tazik2.swedencentral.cloudapp.azure.com/
(no http, but can be pinged)

# Steps performed:
Cloud provider: Azure
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-lamp-stack

- Tazik 1 (tazik1.swedencentral.cloudapp.azure.com / 20.91.130.50):
* installed php7.4, apache2
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04-ru
* cloned and configured to use Tazik2 the KITC app
git clone https://github.com/yurkovskiy/KITC.git

* added SSL let's encrypt certificate
https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04-ru
* installed && configured Moodle 3.11.4
https://linoxide.com/how-to-install-moodle-on-ubuntu-20-04/

- Tazik 2 (tazik2.swedencentral.cloudapp.azure.com / 20.91.139.140):
* installed && configured MySQL 8.0
https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04-ru
