# pg_receivexlog
# Autogenerated from man page /usr/share/man/man1/pg_receivexlog.1.gz
complete -c pg_receivexlog -s D --description 'Directory to write the output to. sp This parameter is required.'
complete -c pg_receivexlog -l if-not-exists --description 'Do not error out when --create-slot is specified and a slot with the specifie…'
complete -c pg_receivexlog -o 'n
.br
--no-loop' --description 'Don\\*(Aqt loop on connection errors.  Instead, exit right away with an error.'
complete -c pg_receivexlog -s s --description 'Specifies the number of seconds between status packets sent back to the serve…'
complete -c pg_receivexlog -s S --description 'Require pg_receivexlog to use an existing replication slot (see Section 26. 2.'
complete -c pg_receivexlog -l synchronous --description 'Flush the WAL data to disk immediately after it has been received.'
complete -c pg_receivexlog -o 'v
.br
--verbose' --description 'Enables verbose mode.'
complete -c pg_receivexlog -s d --description 'Specifies parameters used to connect to the server, as a connection string.'
complete -c pg_receivexlog -s h --description 'Specifies the host name of the machine on which the server is running.'
complete -c pg_receivexlog -s p --description 'Specifies the TCP port or local Unix domain socket file extension on which th…'
complete -c pg_receivexlog -s U --description 'User name to connect as.'
complete -c pg_receivexlog -o 'w
.br
--no-password' --description 'Never issue a password prompt.'
complete -c pg_receivexlog -o 'W
.br
--password' --description 'Force pg_receivexlog to prompt for a password before connecting to a database.'
complete -c pg_receivexlog -l create-slot --description 'Create a new physical replication slot with the name specified in --slot, the…'
complete -c pg_receivexlog -l drop-slot --description 'Drop the replication slot with the name specified in --slot, then exit.'
complete -c pg_receivexlog -o 'V
.br
--version' --description 'Print the pg_receivexlog version and exit.'
complete -c pg_receivexlog -o '?
.br
--help' --description 'Show help about pg_receivexlog command line arguments, and exit.'
complete -c pg_receivexlog -s n --description 'parameter.  OPTIONS.'
complete -c pg_receivexlog -l directory --description '.'
complete -c pg_receivexlog -l no-loop --description '.'
complete -c pg_receivexlog -l status-interval --description '.'
complete -c pg_receivexlog -l slot --description '.'
complete -c pg_receivexlog -s v --description '.'
complete -c pg_receivexlog -l verbose --description '.'
complete -c pg_receivexlog -l dbname --description '.'
complete -c pg_receivexlog -l host --description '.'
complete -c pg_receivexlog -l port --description '.'
complete -c pg_receivexlog -l username --description '.'
complete -c pg_receivexlog -s w --description '.'
complete -c pg_receivexlog -l no-password --description '.'
complete -c pg_receivexlog -s W --description '.'
complete -c pg_receivexlog -l password --description '.'
complete -c pg_receivexlog -s V --description '.'
complete -c pg_receivexlog -l version --description '.'
complete -c pg_receivexlog -s '?' --description '.'
complete -c pg_receivexlog -l help --description '.'

