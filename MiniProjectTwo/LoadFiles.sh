#!/bin/bash
cat recs.txt | sort -u | perl break.pl |  db_load -T -t hash -c dupsort=1 re.idx
cat terms.txt  | sort -u |  perl break.pl | db_load -T -t btree -c dupsort=1 te.idx
cat emails.txt | sort -u | perl break.pl | db_load -T -t btree -c dupsort=1 em.idx
cat dates.txt  | sort -u |  perl break.pl | db_load -T -t btree  -c dupsort=1 da.idx
