__author__ = 'yinjun'

import os
import imp
import time

class SimpleLeetLoader:

    def loadDirs(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        #print os.path.dirname(os.path.abspath(__file__))
        #print os.getcwd()
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

    def execute(self, path):
        pys = os.listdir(path)
        l = len(pys)
        if l == 1:
            file = path + '/' + pys[0]
            os.chdir(path)
            execfile(pys[0])

        elif l == 0:
            print "python file not found in ", path
        else:

            if "solution.py" in pys and "test.py" in pys:
                os.chdir(path)
                execfile("test.py")
            else:
                #print pys
                for i in range(l):
                    print i, pys[i]
                no = raw_input("input file number:")
                j = int(no)
                if j>=0 and j < l:
                    file = path + '/' + pys[j]
                    path = os.getcwd() + '/' + path
                    #execfile(file)
                    #print path
                    os.chdir(path)
                    execfile(pys[j])
                else:
                    print "error python file no "

    def run(self):

        content = raw_input("input problem number (ctrl + x or 0 to exit):")
        #print content
        code = self.loadDirs()

        if content == '0' or content == "":
            exit(1)
        elif content in code:
            path = code[content]
            self.execute(path)
        else:
            print "path not found ", content

    def runWhile(self):

        while True:
            self.run()
            time.sleep(1)

if __name__ == '__main__':
    # service.py executed as script
    # do something
    s = SimpleLeetLoader()
    s.runWhile()