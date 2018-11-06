# iotop
# Autogenerated from man page /usr/share/man/man8/iotop.8.gz
complete -c iotop -l version --description 'Show the version number and exit.'
complete -c iotop -s h -l help --description 'Show usage information and exit.'
complete -c iotop -s o -l only --description 'Only show processes or threads actually doing I/O, instead of showing all pro…'
complete -c iotop -s b -l batch --description 'Turn on non-interactive mode.  Useful for logging I/O usage over time.'
complete -c iotop -s n -l iter --description 'Set the number of iterations before quitting (never quit by default).'
complete -c iotop -s d -l delay --description 'Set the delay between iterations in seconds (1 second by default).'
complete -c iotop -s p -l pid --description 'A list of processes/threads to monitor (all by default).'
complete -c iotop -s u -l user --description 'A list of users to monitor (all by default).'
complete -c iotop -s P -l processes --description 'Only show processes.  Normally iotop shows all threads.'
complete -c iotop -s a -l accumulated --description 'Show accumulated I/O instead of bandwidth.'
complete -c iotop -s k -l kilobytes --description 'Use kilobytes instead of a human friendly unit.'
complete -c iotop -s t -l time --description 'Add a timestamp on each line (implies --batch).'
complete -c iotop -s q -l quiet --description 'suppress some lines of header (implies --batch).'
complete -c iotop -o qq --description 'column names are never printed,.'
complete -c iotop -o qqq --description 'the I/O summary is never printed.'

