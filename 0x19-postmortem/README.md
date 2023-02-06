Below is a postermortem report based on the project webstack debugging 2. Where Nginx is supposed to run as Nginx.

NGINX SERVER OUTAGE INCIDENT REPORT

Issue Summary:

1. Duration of the outage: 45mins
2. Impact: Nginx was not running as Nginx user, leading to failure of access to the webserver. All the users were affected.
3. Root Cause: Nginx was not properly configured to listen to all active IPs on port 8080.

Timeline:

1. 1.00 PM: Configuration push begins
2. 1.10 PM: Outage begins
3. 1.15 PM: Pagers alerted teams
4. 1.20 PM: Debug and file cross-checking
5. 1.30 PM: Server restarts begin
6. 1.45 PM: 100% of traffic back online

Root Cause and Resolution:

The problem was caused by Nginx not being configured to listen on port 8080 of all active IPs. To sort out the issue, a bash script was created that updated the Nginx configuration to listen on all active IPv4 on port 8080 and Nginx was restarted. The script confirmed if Nginx was running and stopped it after it confirmed it was. The script also confirmed that Nginx was listening to port 8080 after starting it.

Corrective and Preventive Measures

Improve on server configuration management to ensure that all necessary ports are open and services are configure correctly.

work on monitoring on the server to alert on any changes to the Nginx configuration and its status.

Occasonally review and update the server configuration by making sure that it is up-to-date and secure.

Tasks:

Update server configuraton management process to include checking for open ports and necessary service configurations.

Implement monitoring on the server to track Nginx configuration and status.

Plan on regular reviews and updates to the server configuration.

Sincerly,

ALX Holberton Cohort-7 Student.
