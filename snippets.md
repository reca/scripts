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
