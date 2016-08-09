# Codesnippets

## mcast
In Python geschriebener Multicastsender und -listener.

## webnotify (''noch nicht fertig'')
In Python geschriebener Check, der Änderungen einer Webseite meldet.
Wenn es funktioniert, soll daraus ein check_mk Plugin werden.

## Ersetzen mehrerer Zeilen
    $ cat /tmp/foo
    foo
    eins
    zwei
    drei
    bar
    $ sed ':a;N;$!ba;s/eins.*drei/vier\nfünf/g' /tmp/foo
    foo
    vier
    fünf
    bar
