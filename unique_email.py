#!/usr/bin/env python3

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_list = []
        for email in emails:
            email_lname, email_domain= email.split('@')
            
            email_localname = email_lname.split('+')[0].replace('.', '')
            email_fname = email_localname+'@'+email_domain
            print(email_fname)
            email_list.append(email_fname)
        print(email_list)
        print(set(email_list))
        return len(set(email_list))  

s = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

a = Solution()
a.numUniqueEmails(s)
print(a)
