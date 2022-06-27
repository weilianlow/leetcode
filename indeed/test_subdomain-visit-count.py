import pytest


class Solution(object):
    def subdomainVisits(self, cpdomains):
        dct = dict()
        for cpdomain in cpdomains:
            v = cpdomain.split(' ')
            count = int(v[0])
            domains = v[1].split('.')
            for i in range(len(domains)):
                domain = '.'.join(domains[i:])
                if dct.get(domain, None) is not None:
                    dct[domain] += count
                else:
                    dct[domain] = count
        return ['{} {}'.format(v, k) for k, v in dct.items()]


@pytest.mark.parametrize("cpdomains, expected", [
    (["9001 discuss.leetcode.com"], ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]),
    (["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
     ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"])])
def test_answer(cpdomains, expected):
    assert sorted(Solution().subdomainVisits(cpdomains)) == sorted(expected)
