for file in *.txt;do
	cat $file >>new.txt
	echo " " >> new.txt
done