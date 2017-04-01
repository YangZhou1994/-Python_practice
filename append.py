import numpy as np
minibatch_inds = []
a = []
for i in xrange(11):
    a.append([])
b = []
for i in range(1, 101):
    b.append(i)

_perm_classified = []
for i in xrange(100):
    c = b[i]/10
    a[c].append(i)
print "############################"
print "array a:"
print a
print "############################"
for i in xrange(11):
    _perm_classified.append([])
for i in range(0, 11):
    _perm_classified[i] = np.random.permutation(xrange(len(a[i])))
_perm_raw = np.random.permutation(xrange(11))
# self._perm = np.random.permutation(xrange(len(self._train_ind[2]) * (2 if self._do_flip else 1)))
_cur = 0
_num_raw = 0
c = []
while True:
    if _cur >= len(a[_perm_raw[_num_raw]]):
        _num_raw += 1
        _cur = 0
    if _num_raw > 10:
        break
    minibatch_inds = []
    #print _perm_raw[_num_raw]
    #print _perm_classified[_perm_raw[_num_raw]][_cur:_cur + 16]
    #print
    #print
    for i in range(_cur, _cur+16 if _cur+16 <= len(_perm_classified[_perm_raw[_num_raw]]) else len(_perm_classified[_perm_raw[_num_raw]])):
        minibatch_inds.append(a[_perm_raw[_num_raw]][_perm_classified[_perm_raw[_num_raw]][i]])
    #minibatch_inds=(a[_perm_raw[_num_raw]][_perm_classified[_perm_raw[_num_raw]][_cur:_cur+5]])
    _cur += 16
    print "minibatch size = %d" %(len(minibatch_inds))
    for i in minibatch_inds:
        c.append(b[i])
        print "b[%d] = %d" %(i+1, b[i])

print "len of b = %d" %(len(b))
print "len of c = %d" %(len(c))
for i in xrange(len(c)):
    print "c[%d] = %d" %(i, c[i])

