class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):

        lst = list(s)
        return self.numDecodingsList(lst, len(lst)-1)

    def numDecodingsList(self, lst, pos):

        if pos < 0:
            return 0
        if pos == 0 :
            if lst[pos] == '0':
                return 0
            else:
                return 1
        else:
            num = int(lst[pos-1] + lst[pos])
            if lst[pos-1] == '0' or lst[pos] == '0' or num >26:
                return self.numDecodingsList(lst, pos -1) + 0
            else:
                return self.numDecodingsList(lst, pos -1) + 1
