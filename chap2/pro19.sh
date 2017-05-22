#uniq -c 重複している行数を先頭に付加する

cut -f1 hightemp.txt | sort | uniq -c | sort -nk1 -r