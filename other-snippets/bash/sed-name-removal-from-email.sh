# This only works in the shell, and for a certain layout. See: http://vanirsystems.com/blog/2010/08/07/removing-names-from-a-list-of-emails/

sed 's/.*&lt;//g' filename.txt &gt; filename.done.txt
