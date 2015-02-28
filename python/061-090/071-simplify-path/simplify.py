class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if path == '' or path == None:
            return '/'
        p = path.split('/')
        r = list()
        c = 0

        for i in range(len(p)):
            if p[i] == '.' or p[i] == '':
                continue
            elif p[i] == '..' and c>0:
                r.pop()
                c-=1
            elif p[i] != '..':
                r.append(p[i])
                c += 1

        return '/'+'/'.join(r)


s = Solution()
print s.simplifyPath("/home/"), "/home"
print s.simplifyPath("/a/./b/../../c/"), "/c"

print s.simplifyPath("/.."), "/"