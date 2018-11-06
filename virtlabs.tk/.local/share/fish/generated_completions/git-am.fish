# git-am
# Autogenerated from man page /usr/share/man/man1/git-am.1.gz
complete -c git-am -s s -l signoff --description 'Add a Signed-off-by: line to the commit message, using the committer identity…'
complete -c git-am -s k -l keep --description 'Pass -k flag to git mailinfo (see git-mailinfo(1)).'
complete -c git-am -l keep-non-patch --description 'Pass -b flag to git mailinfo (see git-mailinfo(1)).'
complete -c git-am -l keep-cr --description 'With --keep-cr, call git mailsplit (see git-mailsplit(1)) with the same optio…'
complete -c git-am -s c -l scissors --description 'Remove everything in body before a scissors line (see git-mailinfo(1)).'
complete -c git-am -l no-scissors --description 'Ignore scissors lines (see git-mailinfo(1)).'
complete -c git-am -s m -l message-id --description 'Pass the -m flag to git mailinfo (see git-mailinfo(1)), so that the Message-I…'
complete -c git-am -l no-message-id --description 'Do not add the Message-ID header to the commit message.'
complete -c git-am -s q -l quiet --description 'Be quiet.  Only print error messages.'
complete -c git-am -s u -l utf8 --description 'Pass -u flag to git mailinfo (see git-mailinfo(1)).'
complete -c git-am -l no-utf8 --description 'Pass -n flag to git mailinfo (see git-mailinfo(1)).'
complete -c git-am -s 3 -l 3way -l no-3way --description 'When the patch does not apply cleanly, fall back on 3-way merge if the patch …'
complete -c git-am -l ignore-space-change -l ignore-whitespace -l whitespace -o 'C<n>' -o 'p<n>' -l directory -l exclude -l include -l reject --description 'These flags are passed to the git apply (see git-apply(1)) program that appli…'
complete -c git-am -l patch-format --description 'By default the command will try to detect the patch format automatically.'
complete -c git-am -s i -l interactive --description 'Run interactively.'
complete -c git-am -l committer-date-is-author-date --description 'By default the command records the date from the e-mail message as the commit…'
complete -c git-am -l ignore-date --description 'By default the command records the date from the e-mail message as the commit…'
complete -c git-am -l skip --description 'Skip the current patch.'
complete -c git-am -s S -l gpg-sign --description 'GPG-sign commits.'
complete -c git-am -l continue -s r -l resolved --description 'After a patch failure (e. g.'
complete -c git-am -l resolvemsg --description 'When a patch failure occurs, <msg> will be printed to the screen before exiti…'
complete -c git-am -l abort --description 'Restore the original branch and abort the patching operation.'
complete -c git-am -s b --description 'flag to git mailinfo (see git-mailinfo(1)).'
complete -c git-am -l no-keep-cr --description 'is useful to override am. keepcr.'
complete -c git-am -s n --description 'flag to git mailinfo (see git-mailinfo(1)).'

