import numpy
import scipy

def binom(n,k):
    # This should be how to caluclate binomial coefficients if you have scipy installed
    
    return scipy.special.binom(n,k)

def findSequence(seq, row, modulus, seq_length, stop_at = 100, row_length = 1):
    # Given a particular sequence and a modulus, will scan over the first stop_at rows looking for it
    
    if row_length >= seq_length:
        for index in range(row_length - seq_length+1):
            if seq == row[index:(index + seq_length)]:
                return (row_length, index)

    if row_length < stop_at:
        row = [0] + row + [0]
        new_row = [(row[i] + row[i+1]) % modulus for i in range(row_length+1)]
        return findSequence(seq, new_row, modulus, seq_length, stop_at, row_length + 1)

    return None

def search(seq, modulus, stop_at = 100, verbose = False):
    # Returns a Boolean representing if search was successful, using mostly calls to findSequence
    
    seq = [element % modulus for element in seq]
    results = findSequence(seq, [1], modulus, len(seq), stop_at)
    if results == None:
        if verbose:
            print("Could not find sequence", seq, "modulo", modulus, "in first", stop_at, "rows.")
        return False
    else:
        if verbose:
            print("In row", results[0]-1, "the sequence", seq, "was found starting at index", results[1])
        return True

def searchFor(n, row, modulus_range, seqs = {}, stop_at = 1000, row_length = 1, last_useful = [1], should_break = True):
    # Given a sequence length and a list of moduli to try, scans through the first stop_at rows recording what it finds in seqs

    if len(last_useful) != len(modulus_range):
        last_useful = [1] * len(modulus_range)
    counter = 0
    for i in range(stop_at):
        useful = False
        if row_length >= n:
            for index in range(row_length - n + 1):
                for i in range(len(modulus_range)):
                    modulus = modulus_range[i]
                    temp = tuple([element % modulus for element in row[index:(index+n)]] + [modulus])
                    if not temp in seqs:
                        last_useful[i] = row_length - 1
                        counter += 1
                        #print(temp)
                    seqs[temp] = seqs.get(temp,[]) + [(row_length-1, index)]
                    

        if row_length < stop_at:
            row = [0] + row + [0]
            row = [row[i] + row[i+1] for i in range(row_length+1)]
            row_length += 1

        if should_break:
            if len(modulus_range) == 1 and counter == modulus_range[0]**n:
                break
            should_continue = False
            for i in range(len(modulus_range)):
                if row_length - last_useful[i] < 100:
                    should_continue = True
                    break
            if not should_continue:
                break
    return (seqs, last_useful)

def rowN(n, modulus):
    row = [1]
    row_length = 1
    for i in range(n):
        row = [0] + row + [0]
        row = [(row[i] + row[i+1]) % modulus for i in range(row_length+1)]
        row_length += 1
    return row

def printToRow(n, modulus):
    row = [1]
    print(0, "\t", row)
    row_length = 1
    for i in range(n):
        row = [0] + row + [0]
        row = [(row[i] + row[i+1]) % modulus for i in range(row_length+1)]
        row_length += 1
        print((i+1), "\t", row)

def allSeqs(n, m):
    if n == 1:
        return [[i] for i in range(m)]
    seqs = allSeqs(n-1,m)
    return [seq + [i] for i in range(m) for seq in seqs]

def allTuples(n, m):
    seqs = allSeqs(n,m)
    return [tuple(seq + [m]) for seq in seqs]

def modDensity(n, m, stop_at = 1000):
    freqs, use = searchFor(n, [1], [m], {}, stop_at, 1, [1], False)
    total = 0
    for seq in freqs:
        total += len(freqs[seq])
    tups = allTuples(n,m)
    #for tup in tups:
#        print("Sequence:", list(tup)[:-1], ", density:", round(len(freqs.get(tup,[]))/total, 3))
    return round(len(freqs.get(tuple([0]*n+[m]), []))/total, 3)

def main():
    # Current just tries the list of primes < 100
    
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    mod_range = primes[:10]
    lengths = range(3,10)
    for n in lengths:
        print("Length:", n)
        freqs, use = searchFor(n, [1], mod_range, {}, 2000)
        for i in range(len(mod_range)):
            m = mod_range[i]
            counter = 0
            tups = allTuples(n, m)
            for tup in tups:
                if freqs.get(tup, 0) != 0:
                    counter += 1
                    #print(tup)
                   # else:
                        #print((i,j), freqs[(i,j,m)])
            print("Mod:", m, ", last useful row:", use[i], ", count of hits:",  counter, ", guess:", n**2 - n + 2)#, ". Percent missed:", round(100*counter/(m**n),2), "%")

#main()
#printToRow(12,3)
#print()
#printToRow(12,3)
#print()
#printToRow(12,6)
#print(rowN(199,2))
mods = range(2,10)
lengths = range(2,10)
rows = [100 * i for i in range(1,21)]
for m in mods:
    for row in rows:
        print("Mod:", m, ", with", row, "rows, density is", modDensity(1,m,row))
#modDensity(1,4,2000)
