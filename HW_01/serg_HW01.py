str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print "a:", str.count("a"), ",", "e:", str.count("e"), ",", "i:", str.count("i"), ",", "o:", str.count("o"), ",", "u:", str.count("u")
print "a:{} e:{} i:{} o:{} u:{}".format(str.count("a"), str.count("e"), str.count("i"), str.count("o"), str.count("u"))
print "e:{1} a:{0} o:{3} u:{4} i:{2}".format(str.count("a"), str.count("e"), str.count("i"), str.count("o"), str.count("u"))

d = "2546,1379"
a = d.index(",")
print a
print (int(d[a-1]+d[a-2]+d[a-3]))