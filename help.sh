printf "ansible-playbook install_geonode.yml --extra-vars \"host=HOSTNAME tmp=TMPDIR home=GEONODE_HOME_DIR dbhome=DATABASE_HOME_DIR gsdata=GEOSERVER_DATA_DIR admin_email=EMAIL admin_pass=PASSWORD sitename=\'Site Name\' orgname=\'Organisation Name\' country=XX target_host=ACTUAL_HOST_NOT_ALIAS\" --step --start-at-task=\"FIRST_TASK\" \n"
printf "\n"
