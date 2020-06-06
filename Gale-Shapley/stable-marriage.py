def unmatched(d): # returns 1 if there exists an unmatched person
    for i in d:
        if(d[i]==-1):
            return 1
    return 0


def unmatch(woman,man,m_watch,w_match):  # breaks match between man and woman
    m_match[man]=-1
    w_match[woman]=-1


def match(woman,man,m_match,w_match):    # matches man and woman
    m_match[man]=woman
    w_match[woman]=man


def get_key(my_dict,val):     # returns key of given value
    for key in my_dict.keys(): 
        if(my_dict[key]==val): 
            return key 
    return "key doesn't exist"


def rate_list(d,man):      # generates preference list 
    L=[0,0,0]
    for v in [1,2,3]:
        L[v-1]=get_key(d[man],v)
    return L


#data
men=['bob', 'jim', 'tom']
women=['ann','lea','sue']


men_rank={'bob':{'ann':2, 'lea':1, 'sue':3},'jim':{'ann':3, 'lea':1, 'sue':2}, 'tom':{'ann':3, 'lea':2, 'sue':1}}
women_rank={'ann':{'bob':3, 'jim':1, 'tom':2}, 'lea':{'bob':2, 'jim':3, 'tom':1}, 'sue':{'bob':3, 'jim':1, 'tom':2}}


w_match={'ann':-1,'lea':-1,'sue':-1}
m_match={'bob':-1,'jim':-1,'tom':-1}


while(unmatched(m_match)==1):
    m=1
    for i in men:
        if(m_match[i]==-1):
            m=i
            break
    L=rate_list(men_rank,m)
    for w in L:
        if(w_match[w]==-1):
            match(w,m,m_match,w_match)
            break
        else:
            m1=w_match[w]
            if(women_rank[w][m1]>women_rank[w][m]):
                unmatch(w,m1,m_match,w_match)
                match(w,m,m_match,w_match)
                break

print("\nFinal stable match: \n",m_match)
