#!/usr/bin/perl
#
# Assumes Mellanox NIC is named as ens6
# Philip.Chan@monash.edu
#
# Usage:
#    ./set_ifcfg.pl [<tmpfilename>]
# To be used within the mlnx_install.sh
#

my $outfile = shift @ARGV;
$outfile = "tmp.ifcfg" if (! defined $outfile);

sub get_index
{
  my $hn = shift;
  my $maxhosts = 32;

  if ($hn =~ /hc(\d+)/) {
    return 33 + $1 if ($1 < $maxhosts);
  }
  if ($hn =~ /hs(\d+)/) {
    return 1 + $1 if ($1 < $maxhosts);
  }
  return 0;
}

my $hostname = `/bin/hostname`;
my $x = get_index($hostname);
die "Unable to parse hostname $hostname" if ($x eq '0');

my $ip = "172.16.229.$x";
print "Assigning $ip to $hostname\n";

open OUT, ">$outfile" or die "Failed to create output file $outfile!";
print OUT "DEVICE=ens6\n";
print OUT "ONBOOT=yes\n";
print OUT "NM_CONTROLLED=no\n";
print OUT "BOOTPROTO=none\n";
print OUT "IPADDR=$ip\n";
print OUT "PREFIX=22\n";
print OUT "MTU=9000\n";
close OUT;

exit 0;
