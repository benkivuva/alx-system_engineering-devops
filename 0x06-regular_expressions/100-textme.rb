#!/usr/bin/env ruby
s = ARGV[0].scan(/from:([^\]]*)|to:([^\]]*)|flags:([^\]]*)/i)
puts [s[0][0], s[1][1], s[2][2]].join(",")
