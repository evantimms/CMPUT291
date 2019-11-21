#!/bin/bash
sort -u terms.txt -o terms.txt |cat terms.txt | perl ./break.pl | db_load -c duplicates=1 -T -t btree terms.idx
sort -u emails.txt -o emails.txt | cat emails.txt | perl ./break.pl | db_load -c duplicates=1 -T -t btree emails.idx
sort -u dates.txt -o dates.txt | cat dates.txt | perl ./break.pl | db_load -c duplicates=1 -T -t btree dates.idx
sort -u recs.txt -o recs.txt | cat recs.txt | perl ./break.pl |  db_load -T -t hash recs.idx