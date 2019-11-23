SSRC="$PWD/hpca23.cse.tamu.edu"
SRC="$SSRC/champsim-traces/CVP"
DST="$PWD/../cvp_traces"
URL="http://hpca23.cse.tamu.edu/champsim-traces/CVP/"

mkdir -p $DST
wget -r --no-parent -A 'public_fp_*.champsimtrace.xz' $URL
wget -r --no-parent -A 'public_int_*.champsimtrace.xz' $URL
rm -r $SRC/fail
cp -r $SRC/* $DST
rm -r $SRC

rm -r $SSRC
