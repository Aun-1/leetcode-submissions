class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #.split -> dictionary #While .find i si no t-1 and infront 
        freq={}
        for i in cpdomains:
            temp=i.split()
            count=int(temp[0])
            domain=temp[1]
            freq[domain]=freq.get(domain,0)+count
            dot_check=domain.find('.')
            while dot_check!=-1:
                domain=domain[dot_check+1:]
                freq[domain]=freq.get(domain,0)+count
                dot_check=domain.find('.')
        result=[]
        for domain in freq:
            result.append(str(freq[domain])+' '+str(domain))
        return result