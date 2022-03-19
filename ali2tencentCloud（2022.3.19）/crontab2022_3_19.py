SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed



* 6 * * * reboot



*/58  *   * * 1-5   /usr/bin/python3.6 /root/FX_daily.py

# only for bonus


*/20  8-14 * * 1-5   /usr/bin/python3.6   /root/following_forbonus_20220104.py





*/12  8-14 * * 1-5   /usr/bin/python3.6   /root/following_js225_400_2022_0211.py
*/17  9-14 * * 1-5   /usr/bin/python3.6   /root/following_js225_400_2022_0211.py
*/22  10-14 * * 1-5   /usr/bin/python3.6   /root/following_js225_400_2022_0211.py






















#us stock







0,10,20,30,40,50  21-23  * * 1-5 /usr/bin/python3 /root/follow_Nas100_2022_02_23.py

0,10,20,30,40,50  0-4  * * 2-6 /usr/bin/python3 /root/follow_Nas100_2022_02_23.py
