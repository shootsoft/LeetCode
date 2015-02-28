__author__ = 'yinjun'

import os

class SimpleLeetLoader:

    def loadDirs(self):
        dirs = os.listdir(os.getcwd())
        code = {}

        for d in dirs:
            #print d
            if os.path.isdir(d) and d!='.idea':
                sub_dirs = os.listdir(d)
                #print sub_dirs
                for s in sub_dirs:
                    path = d+'/'+s
                    #print path
                    if os.path.isdir(path):
                        p = s.index('-')
                        #print p
                        if p >= 0:
                            key = s[0:p]
                            #print key
                            code[key] = path
        return code

    def run(self):
        code = self.loadDirs()

        content = raw_input("input problem number (ctrl + x or 0 to exit):")
        #print content

        if content == '0' or content == "":
            exit(1)
        elif content in code:
            path = code[content]
            pys = os.listdir(path)
            l = len(pys)
            if l == 1:
                file = path + '/' + pys[0]
                execfile(file)
            elif l ==0:
                print "python file not found in ", path
            else:
                #print pys
                for i in range(l):
                    print i, pys[i]
                no = raw_input("input file number:")
                j = int(no)
                if j>=0 and j < l:
                    file = path + '/' + pys[j]
                    print execfile(file)
                else:
                    print "error python file no "
        else:
            print "path not found ", content

    def runWhile(self):

        while True:
            self.run()

if __name__ == '__main__':
    # service.py executed as script
    # do something
    s = SimpleLeetLoader()
    s.runWhile()