# modify file
# execute sed command in shell. Independet of the path

exec {'Modify open files':
     command  => 'sed -i "s/-n 15/-n 2500/g" /etc/default/nginx',
     provider => 'shell'
}
exec {'restart nginx':
     command  => 'service nginx restart',
     provider => 'shell'
}
