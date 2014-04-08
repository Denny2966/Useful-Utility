#-------author:Scr@t-------
#----filename:spider.py----



import sys
import urllib2
import re
import HTMLParser
import wget

class myparser(HTMLParser.HTMLParser):
    ref_count = 0;
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if (tag == 'a'):
            URL = ''
            for name,value in attrs:
                if (name == 'href'):
                    self.ref_count += 1;
                    print self.ref_count;
                    for xx in ['pdf','ppt','pptx','zip','rar']:
                        val = value.find(xx)
                        if val != -1:
                            val0 = value.find('lass');
                            if val0 == -1:
                                value = 'http://lass.cs.umass.edu/~shenoy/courses/spring13/' + value;
                            print value;
                            val2 = re.search('http://',value);
                            val3 = re.search('https://',value);
                            if (val2 != None) | (val3 != None):
                               filename = wget.download(value);
                               fp.write(str(self.ref_count) + ';' + value + ';' + filename + '\n');
#                URL = value[2:]
#                fp.write(sys.argv[2] + URL + '\n')
if sys.argv[1] == '-u':
    content = (urllib2.urlopen(sys.argv[2])).read()
    fp = open("URL.list",'w')
    con = myparser()
    con.feed(content)
else:
    print 'Usage:%s -u url'%sys.argv[0]

