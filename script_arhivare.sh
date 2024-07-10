#!/bin/bash
log_dir="~/curs_devops/bash_scripts/logs"

for file in log_*.log;
do
	if [[ -e $file]];
	then
	       	year_month=$(echo "$file" | awk '{print substr($0, 5, 6)}')
		tar -rvf "${year_month}.tar" "$file"
	fi
done
exit 0
