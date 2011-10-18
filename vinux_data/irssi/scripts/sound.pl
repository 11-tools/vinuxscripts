use strict;
use vars qw($VERSION %IRSSI);

use Irssi;
#set your sound playing method here. suggestionns are paplay or play -q if you have sox installed.
my $soundCommand = "paplay";
$VERSION = '0.0.3';
%IRSSI = (
        authors     => 'Chrelad',
        contact     => 'blah@blah.blah',
        name        => 'alert',
        description => 'Play sounds for different events in IRSSI.',
        url         => 'http://google.com',
        license     => 'GNU General Public License',
        changed     => '$Date: 2007-02-07 12:00:00 +0100 (Thu, 7 Feb 2008) $'
);

#--------------------------------------------------------------------
# Created by Chrelad
# Feb 7, 2008
#modified by Storm Dragon
#Added private message sound and the ability to select sound method
#Sounds now play as a background process.
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# The sound playing function for public message
#--------------------------------------------------------------------

sub pub_msg {
        my ($server,$msg,$nick,$address,$target) = @_;

        my $winitem = $server->window_item_find($target);
        return unless defined $winitem;
        return if $winitem->window() == Irssi::active_win();

        system("$soundCommand /usr/share/irssi/scripts/soundpack/publicmsg.ogg &");
}

#--------------------------------------------------------------------
# The sound playing function for private message
#--------------------------------------------------------------------

sub pri_msg {
        my ($server,$msg,$nick,$address,$target) = @_;


        my $winitem = $server->window_item_find($target);
        return unless defined $winitem;
        return if $winitem->window() == Irssi::active_win();

        system("$soundCommand /usr/share/irssi/scripts/soundpack/privatemsg.ogg &");
}

#--------------------------------------------------------------------
# Irssi::signal_add_last / Irssi::command_bind
#--------------------------------------------------------------------

Irssi::signal_add_last("message public", "pub_msg");
Irssi::signal_add_last("message private", "pri_msg");
#- end
